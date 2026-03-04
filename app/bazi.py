from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def bazi_root():
    return {"service": "bazi", "status": "ok"}
