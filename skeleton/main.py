from fastapi import FastAPI, Body
from llama_cpp import Llama

app = FastAPI()
llm = Llama(model_path="./models/llama-2-7b.ggmlv3.q4_0.bin")

@app.post("/generate")
def generate(prompt: str = Body(...)):
    output = llm(prompt, max_tokens=100)
    return {"response": output["choices"][0]["text"].strip()}
