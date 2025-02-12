import chromadb
import numpy as np
from Backend.embeddings import generate_embeddings
from Backend.vector_db import retrieve_documents
from Backend.llm_handler import generate_response  # New file for LLM handling

#1) Convert Query into an Embedding using  Hugging Face for embeddings. 
#2) Retrieve Top Matching Documents Well perform similarity search in ChromaDB. 
#3) Pass Data to LLM send the retrieved context + query to Hugging Face.


def process_query(query, model_name):
    """Retrieve relevant docs & generate a response."""
    query_embedding = generate_embeddings(query)
    retrieved_texts = retrieve_documents(query_embedding)

    # Format prompt
    prompt = f"Context: {retrieved_texts}\n\nUser Query: {query}\n\nAnswer:"

    # Get response from the selected LLM
    response = generate_response(prompt, model_name)
    return response
