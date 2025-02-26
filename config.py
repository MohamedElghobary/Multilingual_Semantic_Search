import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

VECTOR_SIZE = 768

# Redis Caching Config
REDIS_HOST = "localhost"
REDIS_PORT = 6379
