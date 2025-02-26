from rank_bm25 import BM25Okapi
from embeddings import generate_embedding
from database import qdrant
import config
from cache import get_cached_embedding, cache_embedding

# Retrieve documents from Qdrant
scrolled_points, _ = qdrant.scroll(collection_name=config.COLLECTION_NAME)

# Extract texts from payload
corpus = [doc.payload["text"] for doc in scrolled_points]
bm25 = BM25Okapi([doc.split() for doc in corpus])

def hybrid_search(query, top_k=3):
    # Semantic Search with Embeddings
    cached_embedding = get_cached_embedding(query)
    query_embedding = cached_embedding if cached_embedding else generate_embedding([query])[0].tolist()
    
    if not cached_embedding:
        cache_embedding(query, query_embedding)

    semantic_results = qdrant.search(
        collection_name=config.COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k
    )

    # Return full results (text + score)
    results = [
        {"text": result.payload["text"], "score": round(result.score, 2)}
        for result in semantic_results
    ]
    
    return results
