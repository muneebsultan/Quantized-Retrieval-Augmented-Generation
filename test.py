from essentials import orchestration
from configs import template

# Example usage
model_name = "sentence-transformers/all-MiniLM-L6-v2"
documents_file = "data/documents.pkl"
index_file = "data/faiss_index.bin"
url = "http://localhost:11434"
llm_model_name = "phi3"

orch = orchestration.Orchestration(
    model_name=model_name,
    index_file=index_file,
    documents_file=documents_file,
    prompt_template=template.PROMPT_TEMPLATE,
    llm_url=url,
    llm_model_name=llm_model_name
)

ask = "What is the revenue of apple"
print(orch.run(ask=ask))