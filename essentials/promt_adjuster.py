from langchain_core.prompts.prompt import PromptTemplate

class PromotEngineer:
    def __init__(self, prompt_template):
        self.prompt_template = prompt_template
        print("PE")


    def prompt(self, essentials):
        prompt_adjuster = PromptTemplate(
            input_variables=["data", "question"], template=self.prompt_template
        )

        return prompt_adjuster.format(**essentials)



# PROMPT_TEMPLATE = """Only few words answer
# {data}
# {question}
# """

# prompt_setter = PromotEngineer(prompt_template=PROMPT_TEMPLATE)

# data = {
#     "data": data,
#     "question": ask
# }

# prompted_ask =  prompt_setter.prompt(data)