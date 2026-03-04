from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def chinese_root():
    return {"service": "chinese", "status": "ok"}
