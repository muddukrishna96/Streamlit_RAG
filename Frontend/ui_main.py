import streamlit as st
from Frontend.file_upload import file_upload_component
from Frontend.query_input import query_input_component


def main_ui():
    st.title("📘 Document-based RAG Application")

    # Sidebar for model selection
    st.sidebar.header("Model Selection")
    selected_model = st.sidebar.selectbox(
        "Choose LLM Model",
        ["Mistral", "LLaMA", "Gemma", "Phi"],
        index=0
    )

    # Upload section
    st.subheader("📂 Upload a PDF")
    uploaded_file = file_upload_component()

    # Query section (only if a file is uploaded)
    if uploaded_file:
        st.subheader("🔍 Ask a Question")
        query_input_component(selected_model)
