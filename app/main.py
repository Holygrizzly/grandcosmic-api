from fastapi import FastAPI

from app.western import router as western_router
from app.chinese import router as chinese_router
from app.bazi import router as bazi_router
from app.numerology import router as numerology_router

app = FastAPI(title="GrandCosmic API")

app.include_router(western_router, prefix="/western")
app.include_router(chinese_router, prefix="/chinese")
app.include_router(bazi_router, prefix="/bazi")
app.include_router(numerology_router, prefix="/numerology")


@app.get("/")
def root():
    return {"service": "grandcosmic", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}
