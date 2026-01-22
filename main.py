import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_qdrant import QdrantVectorStore

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

file_path = "./SAchinInfo.pdf"
loader = PyPDFLoader(file_path=file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
)

split_docs = text_splitter.split_documents(documents= docs)


embedder = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001"
)

# vector_store = QdrantVectorStore.from_documents(
#     documents= [], 
#     url = "http://localhost:6333",
#     collection_name = "Learning",
#     embedding=embedder
# )

# vector_store.add_documents(documents = split_docs) 
# print("Injection completed")

retriver = QdrantVectorStore.from_existing_collection(
    url = "http://localhost:6333",
    collection_name = "Learning",
    embedding = embedder
)

relavant_chunk = retriver.similarity_search(
    query = "write all the project name only "
)

system_prompt = """
you are the helpfull AI assistant who responds base of the available context.

context:
{relavant_chunk}

"""