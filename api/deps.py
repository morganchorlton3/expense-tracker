from fastapi import Request
from typing import Generator
from sqlalchemy.orm import Session

def get_db(request: Request) -> Generator[Session, None, None]:
    SessionLocal = request.app.state.sessionmaker
    with SessionLocal() as session:
        yield session
