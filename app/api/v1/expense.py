from fastapi import APIRouter
from app.models.Expense import Expense

router = APIRouter()

@router.get("/", response_model=list[Expense])
def list_all_expenses():
    return []
