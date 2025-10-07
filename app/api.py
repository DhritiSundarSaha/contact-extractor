from fastapi import FastAPI
from pydantic import BaseModel
from app.model import Contact
from app.extractor import gemini_extract_contact

app = FastAPI(title="Contact Extractor API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Contact Extractor API is running!"}

@app.post("/extract", response_model=Contact)
def extract_contact(input: TextInput):
    return gemini_extract_contact(input.text)
