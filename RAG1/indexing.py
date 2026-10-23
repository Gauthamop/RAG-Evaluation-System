from dotenv import load_dotenv
from file_reader import extract_paragraphs
from langchain_core import vectorstores #embedding will be stored at vectorstores 
from langchain_core.vectorstores import InMemoryVectorStore #IN memory vector store
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path



#embedding model is required in this instance 
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_store= InMemoryVectorStore(embeddings)
pdf_path = Path(__file__).resolve().parent.parent / "pdfs" / "Penguins_ACL.pdf"
chunks=extract_paragraphs(pdf_path)

vector_store.add_texts(texts=chunks)
print(f"indexed {len(chunks)} chunks")





load_dotenv()

