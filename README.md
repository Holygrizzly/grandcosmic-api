# grandcosmic-api

GrandCosmic is a FastAPI-based service providing western astrology, Chinese astrology, BaZi, and numerology endpoints.

## Quickstart

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

| Path | Description |
|------|-------------|
| `GET /` | Root status |
| `GET /health` | Health check |
| `GET /western/` | Western astrology service status |
| `GET /chinese/` | Chinese astrology service status |
| `GET /bazi/` | BaZi service status |
| `GET /numerology/` | Numerology service status |