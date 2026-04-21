import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
#import google.generativeai as genai


def create_vectorstore(pdf_paths, api_key):
    documents = []

    # Load multiple PDFs
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)
    
    # Embeddings
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    # Create vector DB
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save locally
    vectorstore.save_local("vectorstore")

    return vectorstore


def load_vectorstore(api_key):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    return FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)


def get_qa_chain(vectorstore, api_key):
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        google_api_key=api_key
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )