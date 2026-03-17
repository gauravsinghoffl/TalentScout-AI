from models.llm_manager import ask_llm
from utils.rag_engine import RAGEngine
from utils.assessment_query_builder import build_assessment_query

rag_engine = RAGEngine()


def generate_questions(candidate_profile):
    role = candidate_profile.get("role", "Software Engineer")
    skills = candidate_profile.get("skills", []) or candidate_profile.get("tech_stack", [])
    experience = candidate_profile.get("experience", "0")

    query = build_assessment_query(candidate_profile)

    retrieved = rag_engine.retrieve(
        query,
        top_k=8,
        filters={
            "role": role,
            "topics": skills,
            "difficulty": "medium"
        }
    )

    retrieved_context = "\n\n".join([
        f"""Reference {i+1}
Topic: {q.get('topic', 'N/A')}
Role: {q.get('role', 'N/A')}
Difficulty: {q.get('difficulty', 'N/A')}
Question: {q.get('question', '')}
"""
        for i, q in enumerate(retrieved)
    ])

    skills_text = ", ".join(skills) if skills else "General software engineering"

    prompt = f"""
You are a senior technical interviewer.

Create exactly 20 INTERMEDIATE-level technical assessment questions for this candidate.

Candidate Role:
{role}

Candidate Skills:
{skills_text}

Experience Level:
{experience} years

Reference questions from knowledge base:
{retrieved_context}

Rules:
- Generate exactly 20 questions
- Questions 1 to 10 must be conceptual/descriptive questions
- Questions 11 to 20 must be multiple choice questions
- Keep all questions relevant to the candidate role and listed skills
- Use the reference questions only for grounding and inspiration
- Do not repeat the reference questions exactly
- Cover all listed skills as evenly as possible
- If multiple skills exist, include several questions from each major skill
- Prioritize the selected role over unrelated technologies
- Ignore unrelated resume technologies
- Do not include soft-skill, HR, or behavioral questions
- Start directly from question 1
- Do not write any introduction, heading, note, or summary
- Do not write phrases like "Here are the questions"
- Output must begin with: 1.

MCQ format must be exactly like this:

11. What does AWS EC2 provide?
A) Storage
B) Virtual servers
C) Monitoring
D) Networking

Now generate the assessment.
"""

    return ask_llm(prompt)