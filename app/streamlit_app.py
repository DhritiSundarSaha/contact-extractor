import streamlit as st
from extractor import gemini_extract_contact
import json
import os

st.set_page_config(page_title="Contact Extractor Chatbot", page_icon="🐶")
st.title("📞 Contact Extractor Chatbot")
st.markdown("**Powered by Taildelights**")

user_input = st.text_area("Paste your messy text here:")

if st.button("Extract Contact"):
    if user_input.strip():
        contact = gemini_extract_contact(user_input)
        contact_data = contact.model_dump()
        st.success("Extracted Contact:")
        st.json(contact_data)
        file_path = "extracted_contacts.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        data.append(contact_data)

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    else:
        st.warning("Please enter some text.")
