import streamlit as st
from extractor import gemini_extract_contact

st.set_page_config(page_title="Contact Extractor Chatbot", page_icon="🐶")
st.title("📞 Contact Extractor Chatbot")
st.markdown("**Powered by Taildelights**")

user_input = st.text_area("Paste your messy text here:")

if st.button("Extract Contact"):
    if user_input.strip():
        contact = gemini_extract_contact(user_input)
        st.success("Extracted Contact:")
        st.json(contact.model_dump())
    else:
        st.warning("Please enter some text.")
