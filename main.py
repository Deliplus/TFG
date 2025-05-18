# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scoring import evaluate_translation

app = FastAPI()

class EvaluationRequest(BaseModel):
    user_scores: dict
    expert_scores: dict

@app.post("/evaluate")
def evaluate(evaluation: EvaluationRequest):
    try:
        result = evaluate_translation(evaluation.user_scores, evaluation.expert_scores)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
