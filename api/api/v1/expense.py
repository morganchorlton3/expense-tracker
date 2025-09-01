from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.deps import get_db
from api.entities.expense import ExpenseORM
from api.models.Expense import ExpenseCreate, ExpenseRead

router = APIRouter()

@router.post("/", response_model=ExpenseRead)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db)):
    obj = ExpenseORM(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj  # Pydantic will read attributes thanks to from_attributes=True

@router.get("/", response_model=list[ExpenseRead])
def list_expenses(limit: int = 100, db: Session = Depends(get_db)):
    rows = db.execute(select(ExpenseORM).order_by(ExpenseORM.posted_at.desc()).limit(limit)).scalars().all()
    return rows
