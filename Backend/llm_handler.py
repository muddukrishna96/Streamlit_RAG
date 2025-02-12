import requests
import os
from urllib.parse import urljoin

# Hugging Face API key
HF_API_KEY = os.getenv("HF_API_KEY")
HF_LLM_API_URL = os.getenv("HF_LLM_API_URL")
def generate_response(prompt, model_name):
    """Query Hugging Face Inference API to generate a response."""
    API_URL = urljoin(HF_LLM_API_URL, model_name)  # Properly joins URL parts
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    payload = {"inputs": prompt, "parameters": {"max_length": 500}}

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        raise Exception(f"Error {response.status_code}: {response.json()}")

