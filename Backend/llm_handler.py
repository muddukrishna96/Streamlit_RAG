import requests
import os
from urllib.parse import urljoin
import time

# Hugging Face API key
HF_API_KEY = os.getenv("HF_API_KEY")
HF_LLM_API_URL = os.getenv("HF_LLM_API_URL")

def generate_response(prompt, model_name):
    """Query Hugging Face Inference API to generate a response."""
    API_URL = urljoin(HF_LLM_API_URL, model_name)  # Properly joins URL parts

    print("api ur after joined ++++++++++++++",API_URL)

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    payload = {"inputs": prompt, "parameters": {"max_length": 500}}

#    response = requests.post(API_URL, json=payload, headers=headers)

#    if response.status_code == 200:
#        return response.json()[0]["generated_text"]
#    else:
#        raise Exception(f"Error {response.status_code}: {response.json()}")
    max_retries=5
    wait_time=10
    for attempt in range(max_retries):
        response = requests.post(API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()[0]["generated_text"]  
        
        elif response.status_code == 503:
            error_message = response.json()
            if "estimated_time" in error_message:
                estimated_time = error_message["estimated_time"]
                print(f"Model is still loading. Estimated wait time: {estimated_time:.2f} seconds.")
                time.sleep(min(wait_time, estimated_time))  # Wait before retrying
            else:
                print(f"Model is still loading. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
        else:
            raise Exception(f"Error {response.status_code}: {response.json()}")

    raise Exception(" Model loading timeout. Try again later.")