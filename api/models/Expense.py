from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ExpenseBase(BaseModel):
    posted_at: datetime
    amount_minor: int
    currency: str = "GBP"
    payee: str | None = None
    category: str | None = None
    notes: str | None = None


class ExpenseCreate(ExpenseBase):
    account_id: str


class ExpenseRead(ExpenseBase):
    id: int
    account_id: str
    model_config = ConfigDict(from_attributes=True)
