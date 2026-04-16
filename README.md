# Quantized Retrieval-Augmented Generation

A compact **retrieval-augmented generation (RAG)** service: dense retrieval with **FAISS**, embeddings from **Hugging Face Transformers**, and answers from a **local LLM** served by **Ollama** (commonly used with **quantized** model weights for efficient CPU/GPU inference). The default use case is **short, grounded answers** over a fixed document corpus (for example, financial Q&A), with retrieval fused into the prompt before generation.

## Architecture

1. **Embed** the user query with a sentence-transformer–style model (`AutoModel` mean pooling).
2. **Retrieve** the top-*k* passages from a prebuilt FAISS index and aligned document list.
3. **Augment** a small prompt template with retrieved context and the question.
4. **Generate** a response via LangChain’s Ollama integration.

The HTTP API is implemented with **FastAPI** and exposes a single query endpoint.

## Requirements

- Python 3.10+ (recommended; match your `torch` wheel if you change versions)
- A running **Ollama** daemon with your chosen chat model pulled
- Precomputed **FAISS index** and **pickled document list** paths (see configuration)

## Configuration

Create a `.env` file in the project root with:

```env
MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2
DOC_FILE_PATH=path/to/documents.pkl
INDEX_FILE_PATH=path/to/faiss_index.bin
LLM_URL=http://localhost:11434
LLM_MODEL_NAME=phi3
```

- `MODEL_NAME`: Hugging Face model id for query (and historically index) embeddings.
- `DOC_FILE_PATH`: Pickle file of documents aligned with the FAISS index rows.
- `INDEX_FILE_PATH`: FAISS index file (e.g. built with the same embedding model as retrieval).
- `LLM_URL` / `LLM_MODEL_NAME`: Ollama base URL and model tag.

## Setup

1. Create and activate a virtual environment.

   **Windows (PowerShell):**

   ```powershell
   python -m venv envs
   .\envs\Scripts\Activate.ps1
   ```

   **Linux / macOS:**

   ```bash
   python -m venv envs
   source envs/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install and start **Ollama**, then pull and run your model (example):

   ```bash
   ollama pull phi3
   ```

   See [Ollama](https://ollama.com/) for platform-specific install steps.

## Run the API

```bash
python app.py
```

The server listens on `0.0.0.0:5000` by default.

## API

**Endpoint:** `POST http://localhost:5000/query`

**Body (JSON):**

```json
{
  "ask": "What is the revenue of Apple?"
}
```

**Response:**

```json
{
  "response": "<model answer string>"
}
```

You can call the same URL from Postman, curl, or any HTTP client.

## Project layout

| Path | Role |
|------|------|
| `app.py` | FastAPI app and `/query` route |
| `essentials/orchestration.py` | Retrieval → prompt → LLM pipeline |
| `essentials/vectors.py` | Embeddings, FAISS search, document loading |
| `essentials/promt_adjuster.py` | LangChain prompt template formatting |
| `essentials/llm.py` | Ollama client via LangChain |
| `configs/template.py` | Default prompt template |
| `__init__.py` | Loads `.env` and exposes config constants |

## Note

Additional notebooks and experiments may live on other branches (for example `dev-hamza`).
