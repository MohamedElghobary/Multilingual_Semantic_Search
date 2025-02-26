import cohere
import numpy as np
import config
from database import qdrant
from qdrant_client.models import PointStruct

co = cohere.Client(config.COHERE_API_KEY)

# Split large text into smaller chunks
def chunk_text(text, chunk_size=200):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

# Generate embeddings
def generate_embedding(texts):
    response = co.embed(texts=texts, model="embed-multilingual-v2.0")
    return np.array(response.embeddings).astype('float32')

# Store text and embeddings in Qdrant
def store_embeddings(texts):
    chunked_texts = [chunk for text in texts for chunk in chunk_text(text)]
    embeddings = generate_embedding(chunked_texts)

    points = [
        PointStruct(id=i, vector=embeddings[i].tolist(), payload={"text": chunked_texts[i]})
        for i in range(len(chunked_texts))
    ]
    
    qdrant.upsert(collection_name=config.COLLECTION_NAME, points=points)
    print(f"✅ Stored {len(chunked_texts)} text chunks in Qdrant.")
