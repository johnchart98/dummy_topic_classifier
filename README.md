# Instagram Topic Classifier

A dummy FastAPI microservice deployed with Docker to Azure App Service.

## Run Locally

```bash
uvicorn app.main:app --reload
```



## Predict Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Enjoying sushi in Tokyo"}'
```
