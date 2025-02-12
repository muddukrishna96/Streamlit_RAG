from Backend.pdf_processing import extract_text_from_pdf
from Backend.embeddings import generate_embeddings
from Backend.vector_db import store_embedding
import numpy as np

def test_pdf_processing():
    print("\n Testing PDF Processing...")
    with open(r"sample.pdf", "rb") as pdf_file:
        md_file = extract_text_from_pdf(pdf_file)
    assert md_file is not None, " PDF processing failed!"
    print(f"✅ PDF text extracted and saved at: {md_file}")

def test_embeddings():
    print("\n🔍 Testing Embeddings Generation...")
    text = "This is a test sentence to generate embeddings."
    embedding = generate_embeddings(text)
    assert embedding is not None and len(embedding) > 0, " Embedding generation failed!"
    print(f"✅ Embeddings generated!  {embedding[:5]}...")

def test_vector_db():
    print("\n🔍 Testing ChromaDB Storage...")
    test_text = "This is a test document for storage."
    test_embedding = np.random.rand(1536)  # Simulating a 1536-dimension vector
    store_embedding("test_doc", test_text, test_embedding)
    print("✅ Data stored in ChromaDB successfully!")

if __name__ == "__main__":
    test_pdf_processing()
    test_embeddings()
    test_vector_db()
    print("\n All backend tests passed successfully!")
