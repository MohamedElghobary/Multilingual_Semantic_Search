from fastapi import FastAPI, Query
from pydantic import BaseModel
from search import hybrid_search
import time
from embeddings import generate_embedding
from database import qdrant
import config
from qdrant_client.models import PointStruct

app = FastAPI()

# Define input model
class TextInput(BaseModel):
    text: str

class SearchInput(BaseModel):
    query: str
    top_k: int = 3  # Default top-k search results

@app.get("/embed/")
def embed(text: str = Query(..., title="Text to Embed")):
    """Generates an embedding for the given text."""
    embedding = generate_embedding([text])[0].tolist()
    return {"text": text, "embedding": embedding}

@app.post("/store/")
def store_text(data: TextInput):
    """Stores the text and its embedding in Qdrant."""
    embedding = generate_embedding([data.text])[0].tolist()
    point_id = int(time.time() * 1000)  # Unique ID using timestamp
    point = PointStruct(id=point_id, vector=embedding, payload={"text": data.text})
    
    qdrant.upsert(collection_name=config.COLLECTION_NAME, points=[point])
    return {"message": "✅ Text stored successfully!", "id": point_id}

@app.get("/search/")
def search(query: str = Query(..., title="Search Query"), top_k: int = Query(3, title="Top K Results")):
    """Performs a hybrid search using the given query."""
    results = hybrid_search(query, top_k)
    return {"query": query, "results": results}
