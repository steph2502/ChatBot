from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyBb1y4PnpUB9oqfbF54znQ95dJoPjNaYTU")

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST", "GET"],
    allow_headers=["*"],
)

# Define a message request model
class Message(BaseModel):
    text: str

# Function to get a response from Gemini AI
def get_gemini_response(user_message):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(user_message)
        return response.text  # Extract the AI-generated response
    except Exception as e:
        return f"Error: {str(e)}"

@app.post("/chat")
def chat(message: Message):
    reply = get_gemini_response(message.text)
    return {"response": reply}
