from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def numerology_root():
    return {"service": "numerology", "status": "ok"}
