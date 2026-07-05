#  NyayaGuide AI

An AI-powered Legal Document Assistant that allows users to upload legal documents, extract text using OCR, and ask questions about the document using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

---

##  Project Overview

Legal documents are often lengthy and difficult to understand. NyayaGuide AI simplifies legal document analysis by allowing users to upload a legal PDF or image and ask questions in natural language. The system extracts text using OCR, processes it using a Retrieval-Augmented Generation (RAG) pipeline, and generates relevant answers with legal insights.

---

##  Features

-  Upload legal PDF documents
-  Upload legal document images
-  OCR-based text extraction using Tesseract
-  Intelligent document chunking
-  AI-powered legal question answering
-  Risk assessment
-  Recommended legal actions
-  FastAPI backend
-  Interactive Swagger API documentation

---

##  Technology Stack

### Backend
- Python
- FastAPI

### AI & NLP
- Groq LLM
- Retrieval-Augmented Generation (RAG)

### OCR
- Tesseract OCR
- OpenCV
- pdf2image
- Poppler

### Libraries
- NumPy
- pytesseract
- OpenCV
- pdf2image

---

##  Project Structure

```
NyayaGuide-AI/
│
├── main.py
├── ocr.py
├── chunking.py
├── rag_engine.py
├── llm_engine.py
├── check_models.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/Hansika1406/nyayaguide-ai.git
```

Go to the project folder

```bash
cd nyayaguide-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install the following software:

- Tesseract OCR
- Poppler for Windows

Update the paths inside `ocr.py` according to your system.

---

## ▶️ Run the Project

Start the FastAPI server

```bash
uvicorn main:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

##  How It Works

1. User uploads a legal document.
2. OCR extracts text from the document.
3. The extracted text is divided into meaningful chunks.
4. Chunks are stored inside the RAG engine.
5. User asks a legal question.
6. Relevant information is retrieved.
7. Groq LLM generates an intelligent response.
8. The system displays:
   - Answer
   - Key legal information
   - Risk level
   - Recommended actions

---

##  API Endpoints

### GET /

Home page

### POST /upload

Upload a legal document

### POST /ask

Ask questions about the uploaded document

---

##  Future Enhancements

- Support for multiple document uploads
- Voice-based legal assistant
- Indian legal act database integration
- Multi-language support
- User authentication
- Chat history
- Document summarization
- Cloud deployment

---

## Team Members

- Hansika Chaudhary
- Tanvi Shekhawat
- Tanishka Sharma

---

##  Project Demo

You can add screenshots of:

- Home Page
- Upload Successful Page
- Question Answer Interface
- Swagger Documentation

inside a `screenshots/` folder.

---

##  License

This project was developed for academic and educational purposes.

---

##  Acknowledgements

- FastAPI
- Groq
- Tesseract OCR
- OpenCV
- Poppler
- Python Community