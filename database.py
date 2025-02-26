from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import config

# Initialize Qdrant Cloud Client
qdrant = QdrantClient(url=config.QDRANT_URL, api_key=config.QDRANT_API_KEY)

# Create Collection Only If It Doesn't Exist
def create_collection():
    try:
        collections_response = qdrant.get_collections()
        existing_collections = [col.name for col in collections_response.collections]

        if config.COLLECTION_NAME not in existing_collections:
            print(f"Creating collection: {config.COLLECTION_NAME} ...")
            qdrant.create_collection(
                collection_name=config.COLLECTION_NAME,
                vectors_config=VectorParams(size=config.VECTOR_SIZE, distance=Distance.COSINE),
            )
            print("Collection created successfully!")
        else:
            print("Collection already exists!")

    except Exception as e:
        print(f"Error checking/creating collection: {e}")

create_collection()
