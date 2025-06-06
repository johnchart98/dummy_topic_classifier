from pydantic import BaseModel

class PostRequest(BaseModel):
    text: str

class TopicProbabilities(BaseModel):
    probabilities: dict