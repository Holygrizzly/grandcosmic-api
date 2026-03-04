from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def western_root():
    return {"service": "western", "status": "ok"}
