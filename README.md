# 📄 RAG Document Reviewer

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions based on their content. The system uses **Google Gemini models + LangChain + FAISS** to retrieve relevant context and generate accurate answers.

---

## 🚀 Features

- 📂 Upload and process PDF documents  
- 🔍 Semantic search using vector embeddings  
- 🤖 AI-powered question answering using Gemini  
- ⚡ Fast retrieval with FAISS vector store  
- 💾 Persistent vector database (local storage)  
- 🧠 Context-aware responses (RAG pipeline)  
- 🎯 Streamlit-based interactive UI  

---

## 🏗️ Project Structure

RAGDocumentReviewer/

├── data/ # Stores input PDF files

├── vectorstore/ # Saved FAISS vector database

├── pycache/ # Python cache files

├── app.py # Streamlit application (UI)

├── rag_pipeline.py # RAG pipeline (embedding + retrieval logic)

├── requirements.txt # Project dependencies

├── .env # API keys (not to be shared)

└── README.md # Project documentation


---

## ⚙️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **LLM**: Google Gemini  
- **Embeddings**: Gemini Embedding Model  
- **Vector DB**: FAISS  
- **Framework**: LangChain  

---

## 🔑 Environment Setup

### 1. Clone the repository
```bash
git clone https://github.com/dhyanisudhanshu01/RAG.git
cd RAG
```
### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
Windows
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Setup API Key

Create a .env file in the root directory:
```bash
GOOGLE_API_KEY=your_api_key_here
```
---
## ▶️ Running the Application
```bash
streamlit run app.py
```
---
## 🧠 How It Works
### 1. Upload PDF documents
### 2. Text is extracted and split into chunks
### 3. Each chunk is converted into embeddings
### 4. Embeddings are stored in FAISS vector database
### 5. User asks a question
### 6. Relevant chunks are retrieved
### 7. Gemini model generates a contextual answer
---
## 📌 Important Notes
- The vectorstore is saved locally for faster reuse
- Ensure .env file is not pushed to GitHub
- If loading saved vectorstore, make sure it is trusted (pickle security)
---
## ⚠️ Known Issues
- Python 3.13 may cause compatibility issues → prefer Python 3.10/3.11
- Embedding model must be correctly set (e.g., gemini-embedding-001)
---
## 📈 Future Improvements
- Add support for multiple file formats
- Implement hybrid search (BM25 + vector search)
- Deploy on cloud (AWS / GCP / HuggingFace Spaces)
- Add chat history & memory
- Improve UI/UX
---
## 🤝 Contributing
- Contributions are welcome! Feel free to fork the repo and submit a pull request.
---
## 📜 License
- This project is open-source and available under the MIT License.
---
## 👨‍💻 Author

## Sudhanshu Dhyani
