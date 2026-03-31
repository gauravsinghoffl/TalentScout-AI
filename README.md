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
  <a href="https://talentscout-ai-app.streamlit.app/">
  <img src="https://img.shields.io/badge/🚀-Live_App-success?style=for-the-badge" />
</a>
</p>

---

## 🚀 Overview

TalentScout AI is an intelligent hiring assistant that automates candidate screening using resume analysis, vector-based retrieval, and AI-driven technical evaluation.

---

## ✨ Features

- 📄 Resume parsing  
- 🧠 Tech stack detection  
- 🔍 FAISS vector retrieval  
- ❓ AI-generated questions  
- 📝 LLM answer evaluation  
- 📊 Final scoring  
- 📑 PDF report generation

---

## 🏗️ Architecture

~~~text
Resume → Extraction → Embeddings → FAISS → Retrieval → LLM → Evaluation → Report
~~~

---

## 📂 Project Structure

```bash
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
    ├── assessment_query_builder.py
    ├── assessment_scorer.py
    ├── final_scorer.py
    ├── pdf_exporter.py
    ├── rag_engine.py
    ├── resume_analyzer.py
    ├── resume_processing.py
    └── validators.py
```

---

## ⚙️ How It Works

1. Upload resume
2. System extracts skills
3. FAISS retrieves relevant questions
4. LLM evaluates responses
5. Final score + report generated

---

## 🛠️ Installation

~~~bash
git clone https://github.com/gauravsinghoffl/TalentScout-AI.git
cd TalentScout-AI

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
~~~

---

## 🔐 Setup

~~~toml
GROQ_API_KEY = "your_api_key"
~~~

---

## ▶️ Run

~~~bash
streamlit run app.py
~~~

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- FAISS  
- Sentence Transformers  
- Groq API  

---

## 📸 Demo Walkthrough

### 📝 1. Candidate Information
![Home](assets/Home Page.png)

### 📄 2. Resume Upload
![Upload](assets/Resume Upload.png)

### 🔍 3. Resume Analysis
![Analysis](assets/Resume Analysis.png)

### ❓ 4. Question Generation
![Questions](assets/Question Generation.png)

### 🧠 5. Technical Assessment (MCQ)
![MCQ](assets/MCQ Question.png)

### 📊 6. Final Report (Hire)
![Hire](assets/Report (Hire).png)

### ⚖️ 7. Final Report (Borderline)
![Borderline](assets/Report (Borderline).png)

### ❌ 8. Final Report (Reject)
![Reject](assets/Report (Reject).png)

### 📑 9. PDF Report Preview
![PDF](assets/PDF Report.png)

---

## 🚀 Future Improvements

- FAISS persistence  
- Better evaluation logic  
- Dashboard  
- Deployment  

---

## 👨‍💻 Author

Gaurav Singh

---

<p align="center">
  Built with ❤️ using Streamlit, FAISS, and LLMs
</p>
