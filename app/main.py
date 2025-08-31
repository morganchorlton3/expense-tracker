from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import expense
from app.db.migrate import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- startup ---
    init_db()
    yield
    # --- shutdown ---

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan
)

app.include_router(expense.router, prefix="/api/v1/expense", tags=["accounts"])
