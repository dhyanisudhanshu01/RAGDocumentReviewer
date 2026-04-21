import streamlit as st
import os
from rag_pipeline import create_vectorstore, load_vectorstore, get_qa_chain
import dotenv

dotenv.load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")


st.set_page_config(page_title="Multi PDF RAG Chatbot", page_icon="🤖")

# api_key = st.secrets["GOOGLE_API_KEY"]

st.title("📄 Chat with Multiple PDFs")

# Upload PDFs
uploaded_file = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=False
)

# Save uploaded PDFs
pdf_paths = []
if uploaded_file:
    os.makedirs("data", exist_ok=True)

    path = os.path.join("data", uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    pdf_paths.append(path)

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Create Vector DB"):
        with st.spinner("Processing PDFs..."):
            st.session_state.vectorstore = create_vectorstore(pdf_paths, api_key)
        st.success("Vector DB created!")

with col2:
    if st.button("Load Existing DB"):
        st.session_state.vectorstore = load_vectorstore(api_key)
        st.success("Loaded existing DB!")

# Chat

if "vectorstore" in st.session_state:
    qa_chain = get_qa_chain(st.session_state.vectorstore, api_key)

    query = st.text_input("Ask a question")

    if query:
        response = qa_chain.run(query)
        st.write(response)