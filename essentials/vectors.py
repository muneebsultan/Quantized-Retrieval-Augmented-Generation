from transformers import AutoTokenizer, AutoModel
import torch
import faiss
import numpy as np
import pickle

class Vector:
    def __init__(self, model_name, index_file, documents_file) :
        self.embed_tokenizer, self.embed_model=self.load_model(model_name)
        self.faiss_index = self.load_index(index_file)
        self.docs = self.load_embedded_documents(documents_file)
        print("Vector")

    def load_model(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)
        return tokenizer, model
    
    def load_index(self, index_file):
        return faiss.read_index(index_file)
    
    def load_embedded_documents(self, documents_file):
        with open(documents_file, 'rb') as f:
            documents = pickle.load(f)
            return documents
        
    def compute_embeddings(self, texts):
        inputs = self.embed_tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = self.embed_model(**inputs)
        embeddings = model_output.last_hidden_state.mean(dim=1)  # mean pooling
        return embeddings.numpy()

    def cosine_search(self, query_embedding, k):
        distances, indices = self.faiss_index.search(query_embedding, k)
        return indices
    
    def search(self, text, k):
        query_embedding = self.compute_embeddings([text])
        retrived_indexes = self.cosine_search(query_embedding, k)
        return [self.docs[i] for i in retrived_indexes[0]]


# model_name = "sentence-transformers/all-MiniLM-L6-v2"
# documents_file = "data/documents.pkl"
# index_file = "data/faiss_index.bin"

# vec = Vector(model_name=model_name,
#                 index_file=index_file,
#                 documents_file=documents_file
#             )

# ask = "What is the revenue of apple"
# data = vec.search(ask, 2)