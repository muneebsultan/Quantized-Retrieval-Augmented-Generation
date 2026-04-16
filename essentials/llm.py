from langchain.llms import Ollama

class LLM:
    def __init__(self, llm_url, llm_model_name):
        self.llm_url = llm_url
        self.llm_model_name = llm_model_name
        print("LLM")


    def ask_to_llm(self, ask):
        ollama = Ollama(base_url=self.llm_url, model=self.llm_model_name)
        return ollama(ask)  


# url = "http://localhost:11434"
# model_name = "phi3"

# llm = LLM(llm_url=url, llm_model_name=model_name)

# # ask = "hi"
# response  = llm.ask_to_llm(prompted_ask)