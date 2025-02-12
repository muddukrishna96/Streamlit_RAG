import os
import streamlit as st
import pdfplumber
from Backend.embeddings import generate_embeddings
from Backend.vector_db import store_embedding
import numpy as np

def save_as_markdown(text, filename, output_dir="Data/markdown"):
    """Save extracted text as a Markdown file."""
    os.makedirs(output_dir, exist_ok=True)
    md_filename = os.path.join(output_dir, f"{filename}.md")
    
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(text)
    
    return md_filename

def process_pdf(uploaded_file):
    """Extract text from uploaded PDF file, save as Markdown, and store in ChromaDB."""
    text = ""
    
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n\n"

    if not text.strip():
        raise ValueError("Could not extract text from PDF! Try another file.")
    
    # Save text as Markdown
    filename = uploaded_file.name.replace(".pdf", "")
    md_file = save_as_markdown(text, filename)

    # Generate & Store Embeddings
    embedding = np.array(generate_embeddings(text))
    store_embedding(filename, text, embedding)
    
    return md_file