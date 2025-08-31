from app.api.v1 import expense
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from app.db.base import Base
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(settings.database_url, echo=settings.debug, pool_pre_ping=True, future=True)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False, future=True)

    # Optional for dev; in prod use Alembic migrations instead
    Base.metadata.create_all(engine)

    app.state.engine = engine
    app.state.sessionmaker = SessionLocal
    try:
        yield
    finally:
        engine.dispose()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan
)

app.include_router(expense.router, prefix="/api/v1/expense", tags=["accounts"])
