import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="Contact Extractor Chatbot", page_icon="🐶")
st.title("📞 Contact Extractor Chatbot")
st.markdown("**Powered by Taildelights**")

# URL of FastAPI server
API_URL = "http://127.0.0.1:8000/extract"

user_input = st.text_area("Paste your messy text here:")

if st.button("Extract Contact"):
    if user_input.strip():
        try:
            # Call FastAPI POST endpoint
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                contact_data = response.json()  
                st.success("Extracted Contact:")
                st.json(contact_data)

                # Save to local JSON file
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
                st.error(f"API returned error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")
    else:
        st.warning("Please enter some text.")
