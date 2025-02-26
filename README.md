Multilingual Semantic Search with Cohere & Qdrant
This project implements a Retrieval-Augmented Generation (RAG) system using Cohere embeddings and Qdrant vector database for efficient semantic search. It provides a FastAPI backend and a Streamlit UI for interaction.

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Set Up Qdrant & Cohere API Keys
Edit config.py and add:

```bash
COHERE_API_KEY = "your-cohere-api-key"
QDRANT_URL = "your-qdrant-cloud-url"
QDRANT_API_KEY = "your-qdrant-api-key"
COLLECTION_NAME = "your-collection"
```


Running the Project

1️⃣ Start the FastAPI Backend

```bash
uvicorn app:app --reload
```
FastAPI will run on http://localhost:8000.

2️⃣ Run the Streamlit UI

```bash
streamlit run ui.py
```
Access the UI at http://localhost:8501.

