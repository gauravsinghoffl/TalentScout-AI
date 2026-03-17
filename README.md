# 🧠 TalentScout AI Hiring Assistant

TalentScout AI is a RAG-based hiring assistant that evaluates candidates using resume analysis, vector-based question retrieval, and AI-driven assessment.

---

## 🚀 Features

- 📄 Resume parsing (PDF)
- 🧠 Tech stack detection
- 🔍 FAISS-based vector retrieval
- ❓ AI-generated technical questions
- 📝 LLM-based answer evaluation
- 📊 Final scoring & hiring recommendation
- 📑 PDF report generation

---

## 🏗️ Architecture

- Sentence Transformers → embeddings
- FAISS → vector similarity search
- Groq (LLM) → generation + evaluation
- Streamlit → UI

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR-USERNAME/TalentScout-AI.git
cd TalentScout-AI

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
