import streamlit as st
import requests

st.title("Multilingual Semantic Search & Embedding")

# --- Search Section ---
st.header("🔍 Search")
query = st.text_input("Enter search query:")
top_k = st.slider("Number of results:", 1, 10, 3)

if st.button("Search"):
    response = requests.get(f"http://localhost:8000/search/", params={"query": query, "top_k": top_k})
    if response.status_code == 200:
        results = response.json().get("results", [])
        for res in results:
            st.write(f"**{res['text']}** (Score: {res['score']:.2f})")
    else:
        st.error("❌ Search failed.")

# --- Embed Section ---
st.header("🧠 Generate Embeddings")
embed_text = st.text_area("Enter text to generate embeddings:")

if st.button("Generate Embedding"):
    response = requests.get(f"http://localhost:8000/embed/", params={"text": embed_text})
    if response.status_code == 200:
        embedding = response.json().get("embedding", [])
        st.success("✅ Embedding generated!")
        st.code(embedding, language="json")
    else:
        st.error("❌ Embedding generation failed.")
        
# --- Store Section ---
st.header("📥 Store Text in Database")
store_text = st.text_area("Enter text to store in the database:")

if st.button("Store Text"):
    response = requests.post("http://localhost:8000/store/", json={"text": store_text})
    if response.status_code == 200:
        st.success("✅ Text stored successfully in Qdrant!")
    else:
        st.error("❌ Failed to store text.")

