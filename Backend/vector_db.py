import chromadb
import numpy as np

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="Data/db")

# Create collection with correct embedding dimension (384)
collection = chroma_client.get_or_create_collection(name="rag_documents", metadata={"hnsw:space": "cosine", "dimension": 384})

def clear_previous_embeddings():
    """Delete all existing embeddings in ChromaDB by fetching all stored IDs."""
    results = collection.get()  # Fetch all stored embeddings
    ids_to_delete = results["ids"]  # Extract document IDs
    
    if ids_to_delete:  # Only delete if there are existing embeddings
        collection.delete(ids=ids_to_delete)

def store_embedding(doc_id, text, embedding):
    """Store embeddings in ChromaDB."""
    clear_previous_embeddings()  # Delete old embeddings before adding new ones
    collection.add(
        ids=[doc_id],
        metadatas=[{"text": text}],
        embeddings=[embedding]  
    )
def retrieve_documents(query_embedding, top_k=3):
    """Retrieve top-k most relevant documents from ChromaDB."""
    results = collection.query(query_embeddings=[ np.array(query_embedding)],n_results=top_k)
    return [doc["text"] for doc in results["metadatas"][0]] if results["metadatas"] else []