import random

TOPICS = [
    "soccer", "food", "travel", "fashion", "fitness",
    "technology", "stockmarket", "movies", "music", "gaming",
    "books", "pets", "nature", "politics", "history",
    "education", "health", "cars", "memes", "relationships"
]

def classify_text(text: str) -> dict:
    probabilities = [random.random() for _ in TOPICS]
    total = sum(probabilities)
    normalized = [round(p / total, 4) for p in probabilities]
    return dict(zip(TOPICS, normalized))