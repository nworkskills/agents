from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent
import uvicorn

app = FastAPI()

class Query(BaseModel):
    prompt: str

@app.post("/ask")
def ask_agent(query: Query):
    return {"response": run_agent(query.prompt)}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)