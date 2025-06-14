import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection("memory")
model = SentenceTransformer("all-MiniLM-L6-v2")

def store_memory(text):
    vec = model.encode([text])[0]
    collection.add(documents=[text], embeddings=[vec], ids=[text[:8]])



