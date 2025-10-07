from fastapi import FastAPI
from app.model import Contact
from app.extractor import gemini_extract_contact

app = FastAPI(title="Contact Extractor API")

@app.get("/")
def root():
    return {"message": "Contact Extractor API is running!"}

@app.post("/extract", response_model=Contact)
def extract_contact(text: str):
    return gemini_extract_contact(text)
