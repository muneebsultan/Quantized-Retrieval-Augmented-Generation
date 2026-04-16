from essentials import vectors, promt_adjuster, llm


class Orchestration(vectors.Vector, promt_adjuster.PromotEngineer, llm.LLM):
    def __init__(self, model_name, index_file, documents_file, prompt_template, llm_url, llm_model_name):
        vectors.Vector.__init__(self, model_name=model_name, index_file=index_file, documents_file=documents_file)
        promt_adjuster.PromotEngineer.__init__(self, prompt_template=prompt_template)
        llm.LLM.__init__(self, llm_url=llm_url, llm_model_name=llm_model_name)

    def run(self, ask):
        # Data Retrieval from Vector DB
        data = self.search(ask, 2)
        
        data_dict = {"data": data, "question": ask}
        
        # Prompt Setter
        prompted_ask = self.prompt(data_dict)
        
        # Response to user
        response = self.ask_to_llm(prompted_ask)
        return response
