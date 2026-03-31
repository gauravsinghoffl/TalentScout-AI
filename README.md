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

TalentScout AI is an AI-powered hiring assistant that automates end-to-end candidate evaluation using a Retrieval-Augmented Generation (RAG) pipeline. It processes resumes, extracts skills, generates embeddings using sentence transformers, retrieves relevant context through FAISS vector search, and leverages LLMs to generate technical questions and evaluate responses. The system then produces structured candidate scores and detailed PDF reports, enabling efficient and scalable recruitment workflows.


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

## 🏗️ System Architecture

```mermaid
flowchart TD

    %% UI Layer
    A[Candidate Input Form]
    B[Resume Upload]
    C[Assessment Interface]
    D[Results Display]

    %% Processing
    E[Resume Parsing]
    F[Skill Extraction]
    G[Text Preprocessing]

    %% AI / RAG
    H["Embeddings Generation (Sentence Transformers)"]
    I[FAISS Vector Search]
    J[RAG Context Retrieval]
    K[LLM Question Generation]
    L[LLM Answer Evaluation]

    %% Output
    M[Scoring Engine]
    N[Report Generation]
    O[PDF Export]

    %% Flow
    A --> B
    B --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> C
    C --> L
    L --> M
    M --> N
    N --> O
    O --> D

    %% External
    P[Groq API / LLM]
    P --> K
    P --> L
```
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

- **Language:** Python  
- **Frontend/UI:** Streamlit  
- **AI/ML:** NLP, Sentence Transformers, LLMs  
- **RAG Pipeline:** Retrieval-Augmented Generation  
- **Vector Search:** FAISS  
- **LLM Inference:** Groq API  
- **Data Processing:** Resume parsing & text extraction  
- **Output Generation:** PDF report generation  

---

## 📸 Demo Walkthrough
<br>

### 📝 1. Candidate Information
![Home](assets/Home%20Page.png)
<br><br>

### 📄 2. Resume Upload
![Upload](assets/Resume%20Upload.png)
<br><br>

### 🔍 3. Resume Analysis
![Analysis](assets/Resume%20Analysis.png)
<br><br>

### ❓ 4. Question Generation
![Questions](assets/Question%20Generation.png)
<br><br>

### 🧠 5. MCQ Type Question
![MCQ](assets/MCQ%20Question.png)
<br><br>

### 📊 6. Final Report (Hire)
![Hire](assets/Report%20%28Hire%29.png)
<br><br>

### ⚖️ 7. Final Report (Borderline)
![Borderline](assets/Report%20%28Borderline%29.png)
<br><br>

### ❌ 8. Final Report (Reject)
![Reject](assets/Report%20%28Reject%29.png)
<br><br>

### 📑 9. PDF Report Preview
![PDF](assets/PDF%20Report.png)

---

## 🚀 Future Improvements

- Implement persistent FAISS index to optimize retrieval performance  
- Enhance evaluation logic using more robust LLM-based scoring
- Authentication & User Management system
- Multi-format Resume Support (DOCX, OCR)
- API Integration for ATS systems
- Develop a recruiter dashboard for tracking candidate performance  
- Deploy the application on cloud platforms for scalability  

---

## 👨‍💻 Author

Gaurav Singh

---

<p align="center">
  Built with ❤️ using Streamlit, FAISS, and LLMs
</p>
