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

TalentScout AI is an intelligent hiring assistant that automates candidate screening using resume analysis, vector-based retrieval, and AI-driven technical evaluation.

---

## ✨ Features

- 📄 Resume parsing  
- 🧠 Tech stack detection  
- 🔍 FAISS vector retrieval  
- ❓ AI-generated questions  
- 📝 LLM answer evaluation  
- 📊 Final scoring  
- 📑 PDF reports  

---

## 🏗️ Architecture

~~~text
Resume → Extraction → Embeddings → FAISS → Retrieval → LLM → Evaluation → Report
~~~

---

## 📂 Project Structure

~~~bash
TalentScout-AI/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── assessment/
├── components/
├── config/
├── data/
├── models/
├── reporting/
├── utils/
~~~

---

## ⚙️ Installation

~~~bash
git clone https://github.com/YOUR-USERNAME/TalentScout-RAG-AI.git
cd TalentScout-RAG-AI

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

## 🚀 Future Improvements

- FAISS persistence  
- Better evaluation logic  
- Dashboard  
- Deployment  

---

## 👨‍💻 Author

Your Name

---

<p align="center">
  Built with ❤️ using Streamlit, FAISS, and LLMs
</p>
