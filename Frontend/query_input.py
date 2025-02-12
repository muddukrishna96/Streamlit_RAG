import streamlit as st

def query_input_component(model_name):
    st.subheader("🔍 Ask a Question from the Document")

    # Text input for user query
    query = st.text_input("Enter your question:", placeholder="E.g., What is the summary of this document?")

    # Button to fetch the response
    if st.button("Get Answer"):
        if query.strip():
            response = f"🔮 Model ({model_name}) says: This is a placeholder response."
            st.info(response)
        else:
            st.warning(" Please enter a query before submitting!")

