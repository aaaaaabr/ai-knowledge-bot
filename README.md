![MIT License](https://img.shields.io/badge/license-MIT-blue)
![Built with LangChain](https://img.shields.io/badge/Built%20with-LangChain-4b7bec)
![Offline AI](https://img.shields.io/badge/LLM-Ollama-green)
![last commit](https://img.shields.io/github/last-commit/EzioDEVio/ai-knowledge-bot?color=blue)
![repo size](https://img.shields.io/github/repo-size/EzioDEVio/ai-knowledge-bot)
![GitHub issues](https://img.shields.io/github/issues/EzioDEVio/ai-knowledge-bot)
![Forks](https://img.shields.io/github/forks/EzioDEVio/ai-knowledge-bot?style=social)
![Stars](https://img.shields.io/github/stars/EzioDEVio/ai-knowledge-bot?style=social)
![PRs](https://img.shields.io/github/issues-pr/EzioDEVio/ai-knowledge-bot)

# 🧠 AI Knowledge Bot

This is my own custom-built offline AI bot that lets you chat with PDFs and web pages using **local embeddings** and **local LLMs** like LLaMA 3.

I built it step by step using LangChain, FAISS, HuggingFace, and Ollama — without relying on OpenAI or DeepSeek APIs anymore (they just kept failing or costing too much).

---

## 🚀 Features

- 📄 Chat with uploaded PDF files
- 🌍 Ask questions about a webpage URL
- 🧠 Uses local HuggingFace embeddings (`all-MiniLM-L6-v2`)
- 🦙 Powered by Ollama + LLaMA 3 (fully offline LLM)
- 🗃️ Built-in FAISS vectorstore
- 🧾 PDF inline preview
- 🧮 Built-in calculator + summarizer tools (via LangChain agents)
- 🧠 Page citation support (know where each answer came from)
- 📜 Chat history viewer with download button (JSON)
- 🎛️ Simple Streamlit UI with dark/light mode toggle
- 👨‍💻 Footer credit: *Developed by EzioDEVio*

---

## 📦 Tech Stack

- `langchain`, `langchain-community`
- `sentence-transformers` for local embeddings
- `ollama` for local LLMs (`llama3`)
- `PyPDF2` for PDF parsing
- `FAISS` for vector indexing
- `Streamlit` for frontend

---

## 🛠 Setup Guide

### 1. Clone this repo

```bash
git clone https://github.com/EzioDEVio/ai-knowledge-bot.git
cd ai-knowledge-bot
````

---

### 2. Create and activate virtualenv (optional but recommended)

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows for Mac is different
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure `sentence-transformers` is installed — needed for local embeddings.

---

### 4. Install Ollama (for local LLM)

Download and install from:

👉 [https://ollama.com/download](https://ollama.com/download)

After installation, verify:

```bash
ollama --version
```

Then pull and run the model:

```bash
ollama run llama3
```

> This will download the LLaMA 3 model (approx. 4–8GB). You can also try `mistral`, `codellama`, etc.

---

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at:

```
http://localhost:8501
```

---

## 📁 Folder Structure

```
ai-knowledge-bot/
├── app.py                     # Main Streamlit UI
├── backend/
│   ├── pdf_loader.py          # PDF text extraction
│   ├── web_loader.py          # Webpage scraper
│   ├── vector_store.py        # Embedding + FAISS
│   └── qa_chain.py            # LLM QA logic (Ollama + tools)
├── .env                       # Not used anymore (was for API keys)
├── requirements.txt
└── README.md
```

---

## ✅ Working Setup Summary

| Component        | Mode                                 |
| ---------------- | ------------------------------------ |
| Embeddings       | Local (`HuggingFace`)                |
| Vectorstore      | Local (`FAISS`)                      |
| LLM Response     | Local (`Ollama` + `llama3`)          |
| Internet Needed? | ❌ Only for first-time model download |

---

## ⚠️ Why I Avoided OpenAI / DeepSeek

* **OpenAI** failed with `RateLimitError` and quota issues unless I added billing.
* **DeepSeek** embedding endpoints didn’t work — only chat models supported.

So I switched to:

* 🔁 Local `HuggingFaceEmbeddings` for vectorization
* 🦙 `ChatOllama` for full offline AI answers

---

## ✅ Now Completed Features

* ✅ PDF upload + preview
* ✅ URL content QA
* ✅ Chat history with page citations
* ✅ Calculator + summarizer tools
* ✅ Footer attribution
* ✅ JSON export
* ✅ 100% offline functionality


---

## 🐳 Run with Docker (Secure Production Mode)

Build and run the app securely using a **multi-stage Dockerfile**:

 1. Build the container

```bash
docker build -t ai-knowledge-bot .
```


2. Run the container
Make sure Ollama is running on the host, open up a powershell or in different terminal then:

docker run -p 8501:8501 \
  --add-host=host.docker.internal:host-gateway \
  ai-knowledge-bot
---
## 🔐 Dockerfile Security Highlights
✅ Multi-stage build (separates dependencies from runtime)

✅ Minimal base (python:3.10-slim)

✅ Non-root appuser by default

✅ .env, venv, logs excluded via .dockerignore

✅ Exposes only necessary port (8501)

✅ Automatically starts Streamlit app

---
## 💬 License

MIT — feel free to fork, use, or improve it.

---

## 🔥 Built by EzioDEVio | 🇮🇶 | 🧠

From concept to offline AI — all step by step.

---

