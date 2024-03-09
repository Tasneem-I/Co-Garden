'''from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_path, chunk_size=500, chunk_overlap=20):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap))
    return pages

pdf_path = "data\garden.pdf"
split_docs = load_and_split_pdf(pdf_path)
#print(len(split_docs))

from langchain.embeddings import SentenceTransformerEmbeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")'''









'''from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone
from pinecone import Pinecone, PodSpec

# Initialize Pinecone
pc = Pinecone(api_key='86fab667-d7c5-4080-8689-77ae62444fcd')
spec=PodSpec(environment="gcp-starter")
index_name="cogardens"
index = pc.Index(index_name)
print(index.describe_index_stats())
# Load and split the PDF
def load_and_split_pdf(pdf_path, chunk_size=500, chunk_overlap=20):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap))
    return [page.page_content for page in pages]

pdf_path = "data\garden.pdf"
split_docs = load_and_split_pdf(pdf_path)

# Embed the documents using a pre-trained model
from sentence_transformers import SentenceTransformer
import torch
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(split_docs)

# Convert the numpy arrays to tensors

# Convert the numpy arrays to PyTorch tensors

# Convert the padded_embeddings tensor to a list of tuples
flattened_embeddings = embeddings = [list(embedding) for embedding in model.encode(split_docs)]
# Upsert the embeddings into Pinecone
ids = list(range(len(embeddings)))
index.upsert(ids=ids, vectors=embeddings)
print(index.describe_index_stats())'''



from langchain_community.document_loaders import DirectoryLoader

directory = 'data'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
print(len(documents))
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
print(len(docs))

from langchain_community.embeddings import SentenceTransformerEmbeddings
import os
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
pinecone_api_key = os.environ.get('PINECONE_API_KEY')
from pinecone import Pinecone, PodSpec
from langchain_pinecone import PineconeVectorStore
pc = Pinecone(api_key=pinecone_api_key)
spec=PodSpec(environment='gcp-starter')
index_name='cogardens'
indexsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)
index = pc.Index(index_name)
print(index.describe_index_stats())
