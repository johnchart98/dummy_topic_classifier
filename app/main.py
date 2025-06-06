from fastapi import FastAPI
from app.schemas import PostRequest, TopicProbabilities
from app.model import classify_text

app = FastAPI(title="Instagram Topic Classifier")

@app.post("/predict", response_model=TopicProbabilities)
def predict(post: PostRequest):
    probs = classify_text(post.text)
    return {"probabilities": probs}