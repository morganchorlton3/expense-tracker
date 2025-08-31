from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import expense

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.include_router(expense.router, prefix="/api/v1/expense", tags=["accounts"])
