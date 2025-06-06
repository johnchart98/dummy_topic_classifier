# Instagram Topic Classifier

A dummy FastAPI microservice deployed with Docker to Azure App Service.

## Run Locally

```bash
uvicorn app.main:app --reload
```

## Docker Run

```bash
docker build -t topic-classifier .
docker run -p 8000:80 topic-classifier
```

## Predict Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Enjoying sushi in Tokyo"}'
```