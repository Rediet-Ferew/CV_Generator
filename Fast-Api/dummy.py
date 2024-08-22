
import requests
import json
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

payload = {
     "inputs": "Generate profile section in resume for the job Graphic Designer"
}
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Generate profile section in resume for the job Graphic Designer",
})

print(output)