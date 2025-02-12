import requests
import os
import time
# Set your Hugging Face API key

HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = os.getenv("API_URL")

def generate_embeddings(text, max_retries=5, wait_time=10):
    """Generate embeddings using Hugging Face Inference API."""
    
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    payload = text  # Send raw string

    for attempt in range(max_retries):
            response = requests.post(API_URL, json=payload, headers=headers)

            if response.status_code == 200:
                return response.json()  # Returns a list of embeddings
            
            elif response.status_code == 503:
                error_message = response.json()
                if "estimated_time" in error_message:
                    estimated_time = error_message["estimated_time"]
                    print(f"⚠️ Model is still loading. Estimated wait time: {estimated_time:.2f} seconds.")
                    time.sleep(min(wait_time, estimated_time))  # Wait before retrying
                else:
                    print(f"⚠️ Model is still loading. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
            else:
                raise Exception(f"Error {response.status_code}: {response.json()}")

    raise Exception(" Model loading timeout. Try again later.")




