from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
# model_name = "sentence-transformers/all-MiniLM-L6-v2"
# documents_file = "data/documents.pkl"
# index_file = "data/faiss_index.bin"
# url = "http://localhost:11434"
# llm_model_name = "phi3"



MODEL_NAME = os.getenv('MODEL_NAME')
DOC_FILE_PATH = os.getenv('DOC_FILE_PATH')
INDEX_FILE_PATH = os.getenv('INDEX_FILE_PATH')
LLM_MODEL_NAME = os.getenv('LLM_MODEL_NAME')
LLM_URL = os.getenv('LLM_URL')

print(MODEL_NAME)
print(DOC_FILE_PATH)
print(INDEX_FILE_PATH)
print(LLM_MODEL_NAME)