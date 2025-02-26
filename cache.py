import redis
import json
import config

# Initialize Redis Client
redis_client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

# Cache embeddings
def cache_embedding(query, embedding):
    redis_client.set(query, json.dumps(embedding))

# Retrieve from cache
def get_cached_embedding(query):
    cached = redis_client.get(query)
    return json.loads(cached) if cached else None
