from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AdvisorFlow AI")

class PrepRequest(BaseModel):
  client_id: str
  style: str = "executive"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-prep-brief")
def generate_prep_brief(request: PrepRequest):
    return {"client_id": request.client_id, "brief": "Prep brief will be generated here."}