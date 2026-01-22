
#  PDF Question Answering System using Gemini + Qdrant (RAG)

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows you to ask questions about a PDF file and get accurate answers using **Google Gemini**, **LangChain**, and **Qdrant vector database**.

---

##  Features

* Load and read PDF files
* Split text into chunks
* Generate embeddings using **Gemini**
* Store & search vectors in **Qdrant**
* Retrieve relevant context
* Answer questions using **Gemini LLM**

---

##  Tech Stack

* Python 3.9+
* LangChain
* Google Gemini (via OpenAI-compatible API)
* Qdrant (Vector DB)
* dotenv
* PyPDF
* Recursive Text Splitter

---

## Project Structure

```text
.
├── SAchinInfo.pdf
├── main.py
├── .env
├── README.md
```

---

##  Environment Setup

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

##  Install Dependencies

```bash
pip install langchain langchain-community langchain-qdrant langchain-google-genai \
            python-dotenv pypdf openai qdrant-client
```

---

##  Run Qdrant (Docker)

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

##  First-Time Vector Injection

Uncomment this part once:

```python
vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="Learning",
    embedding=embedder
)

vector_store.add_documents(documents=split_docs)
print("Injection completed")
```

Run the script once to store embeddings.

Then **comment it again**.

---

## ▶ Run the App

```bash
python main.py
```

You will see:

```
ask a question..
```

Type your question about the PDF.

---

##  Working

1. Loads PDF
2. Splits into chunks
3. Converts chunks to embeddings
4. Stores in Qdrant
5. Searches similar chunks
6. Sends context + question to Gemini
7. Returns a grounded answer

---

##  Example

```text
ask a question..
Who is Sachin?
```

**Output:**

> Sachin is a software engineer with experience in Python, AI, and backend development...


