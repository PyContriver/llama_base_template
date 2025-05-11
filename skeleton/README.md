# {{ name }}

A FastAPI application with LLaMA integration using `llama-cpp-python`.

## Running

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoint

- POST `/generate` with JSON: `{ "prompt": "Your question here" }`
