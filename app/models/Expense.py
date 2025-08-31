from pydantic import BaseModel

class Expense(BaseModel):
    id: str
    name: str
    amount: float
    category: str
