import re
import phonenumbers
from email_validator import validate_email, EmailNotValidError
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model import Contact

def gemini_extract_contact(text: str):
    #using regex
    name = re.search(r"(?:Mr\.|Ms\.|Dr\.|[A-Z][a-z]+)\s+[A-Z][a-z]+", text)
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    phone = re.search(r"\+?\d[\d\s\-\(\)]{8,}\d", text)
    age = re.search(r"(\d{1,3})\s*year[s]?(?:\s*old)?", text, re.IGNORECASE)

    contact = Contact(
        name=name.group() if name else None,
        email=clean_email(email.group()) if email else None,
        phone=clean_phone(phone.group()) if phone else None,
        age=int(age.group(1)) if age else None
    )
    return contact

def clean_phone(phone):
    try:
        number = phonenumbers.parse(phone, "IN")
        return phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    except:
        return None

def clean_email(email):
    try:
        v = validate_email(email)
        return v.email
    except EmailNotValidError:
        return None
