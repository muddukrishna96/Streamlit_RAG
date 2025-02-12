import streamlit as st
from Frontend.file_upload import file_upload_component
from Backend.pdf_processing import process_pdf
from Backend.query_processing import process_query

def main_ui():
    st.title("📘 Document-based RAG Application")

    # Upload section
    st.subheader("📂 Upload a PDF")
    uploaded_file = file_upload_component()

    if uploaded_file:
    # Save & Process PDF
        with st.spinner("Processing PDF..."):
            pdf_text = process_pdf(uploaded_file)
        st.success("PDF Processed & Stored!")

    user_query = st.text_input("Ask a question about the document:")
    model_name = st.selectbox("Choose LLM Model", ["google/flan-t5-small", "google/flan-t5-base"])

    if st.button("Get Answer"):
        if user_query.strip():
            with st.spinner("Retrieving & Generating Response..."):
                response = process_query(user_query, model_name)
            st.write("### AI Response:")
            st.success(response)
        else:
            st.warning("Please enter a query.")