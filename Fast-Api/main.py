from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Replace with your Hugging Face API key
API_KEY = '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'
MODEL_NAME = 'gpt2'

# Define the API URL
API_URL = f"https://api-inference.huggingface.co/models/openai-community/gpt2"

class TextRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(request: TextRequest):
    # Define headers with API key
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

    # Define payload
    data = {
        "inputs": request.prompt
    }

    # Make the request to Hugging Face API
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        return {"generated_text": result}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
