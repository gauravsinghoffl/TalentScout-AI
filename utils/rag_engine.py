import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class RAGEngine:
    def __init__(self, question_file="data/technical_questions.json"):
        # Load embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Load question dataset
        with open(question_file, "r", encoding="utf-8") as f:
            self.questions = json.load(f)

        # Build structured documents
        self.documents = [self._build_document(q) for q in self.questions]

        # Generate embeddings (ONLY ONCE)
        embeddings = self.model.encode(
            self.documents,
            convert_to_numpy=True,
            normalize_embeddings=True
        ).astype("float32")

        # Create FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

    # -----------------------------------
    # Build structured document
    # -----------------------------------
    def _build_document(self, q):
        return f"""
Topic: {q.get('topic', '')}
Role: {q.get('role', '')}
Difficulty: {q.get('difficulty', '')}
Question: {q.get('question', '')}
""".strip()

    # -----------------------------------
    # Retrieval function (OPTIMIZED)
    # -----------------------------------
    def retrieve(self, query, top_k=5, filters=None):
        # 1. Encode query
        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        ).astype("float32")

        # 2. Search full FAISS index
        scores, indices = self.index.search(query_embedding, top_k * 5)

        results = []
        seen = set()

        for idx in indices[0]:
            item = self.questions[idx]

            # 3. Apply filters AFTER retrieval
            if filters:
                role = filters.get("role")
                topics = filters.get("topics")
                difficulty = filters.get("difficulty")

                if role and item.get("role", "").strip().lower() != role.strip().lower():
                    continue

                if topics:
                    topic_set = {t.strip().lower() for t in topics if t.strip()}
                    if item.get("topic", "").strip().lower() not in topic_set:
                        continue

                if difficulty and item.get("difficulty", "").strip().lower() != difficulty.strip().lower():
                    continue

            # 4. Deduplicate questions
            q_text = item.get("question", "").strip().lower()

            if q_text not in seen:
                results.append(item)
                seen.add(q_text)

            # 5. Stop when enough results
            if len(results) >= top_k:
                break

        # 6. Fallback if nothing found
        if not results:
            return self.questions[:top_k]

        return results