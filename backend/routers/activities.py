from fastapi import APIRouter
from backend.sheets_client import fetch_data

router = APIRouter(
    prefix="/activities",
    tags=["activities"]
)

@router.get("/")
def get_activities():
    return fetch_data()