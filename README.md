<h1 align="center">🧠 TalentScout AI Hiring Assistant</h1>

<p align="center">
  RAG-based AI hiring assistant using FAISS vector search, sentence-transformer embeddings, and LLM-powered candidate evaluation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-Enabled-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Groq-purple?style=for-the-badge" />
</p>

---

## 🚀 Overview

TalentScout AI is an intelligent hiring assistant that automates candidate screening through:

- 📄 Resume parsing
- 🧠 Tech stack detection
- 🔍 RAG-based question retrieval
- ❓ AI-generated technical assessments
- 📝 LLM-based answer evaluation
- 📊 Final candidate scoring
- 📑 PDF report export

---

## 🏗️ Architecture

```text
Resume PDF
   ↓
Text Extraction
   ↓
Skill Detection
   ↓
Sentence-Transformer Embeddings
   ↓
FAISS Vector Retrieval
   ↓
LLM Question Generation
   ↓
Answer Evaluation
   ↓
Final Score + Hiring Recommendation

---

<h1 align="center">🧠 TalentScout AI Hiring Assistant</h1>

<p align="center">
  RAG-based AI hiring assistant using FAISS vector search, sentence-transformer embeddings, and LLM-powered candidate evaluation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-Enabled-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Groq-purple?style=for-the-badge" />
</p>

---

## 🚀 Overview

TalentScout AI is an intelligent hiring assistant that automates candidate screening through:

- 📄 Resume parsing
- 🧠 Tech stack detection
- 🔍 RAG-based question retrieval
- ❓ AI-generated technical assessments
- 📝 LLM-based answer evaluation
- 📊 Final candidate scoring
- 📑 PDF report export

---

## 🏗️ Architecture

```text
Resume PDF
   ↓
Text Extraction
   ↓
Skill Detection
   ↓
Sentence-Transformer Embeddings
   ↓
FAISS Vector Retrieval
   ↓
LLM Question Generation
   ↓
Answer Evaluation
   ↓
Final Score + Hiring Recommendation

---

✨ Features

Resume upload and PDF text extraction

Technical skill detection from resume

FAISS-backed vector retrieval

LLM-generated technical questions

LLM-based answer scoring

Final hiring recommendation system

Downloadable PDF candidate report

---

📂 Project Structure

TalentScout-AI/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── assessment/
│   ├── answer_evaluator.py
│   └── question_generation.py
│
├── components/
│   ├── progress.py
│   └── sidebar.py
│
├── config/
│   ├── constants.py
│   └── settings.py
│
├── data/
│   └── technical_questions.json
│
├── models/
│   └── llm_manager.py
│
├── reporting/
│   └── report_generator.py
│
├── utils/
│   ├── assessment_query_builder.py
│   ├── assessment_scorer.py
│   ├── final_scorer.py
│   ├── pdf_exporter.py
│   ├── rag_engine.py
│   ├── resume_analyzer.py
│   ├── resume_processing.py
│   └── validators.py


---

⚙️ Installation

git clone https://github.com/YOUR-USERNAME/TalentScout-RAG-AI.git
cd TalentScout-RAG-AI

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

