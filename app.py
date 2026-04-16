from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from essentials.orchestration import Orchestration

from configs.template import PROMPT_TEMPLATE
from __init__ import MODEL_NAME, DOC_FILE_PATH, INDEX_FILE_PATH, LLM_MODEL_NAME, LLM_URL


app = FastAPI()

class Query(BaseModel):
    ask: str

orch = Orchestration(
    model_name=MODEL_NAME,
    index_file=INDEX_FILE_PATH,
    documents_file=DOC_FILE_PATH,
    prompt_template=PROMPT_TEMPLATE,
    llm_url=LLM_URL,
    llm_model_name=LLM_MODEL_NAME
)


@app.post("/query")
async def get_response(query: Query):
    ask = query.ask
    try:
        response = orch.run(ask=ask)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
