import streamlit as st

def file_upload_component():
    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])
    
    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")
        return uploaded_file
    return None
