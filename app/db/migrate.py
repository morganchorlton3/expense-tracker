from app.db.postgres import engine
from app.db.base import Base
from app.entities.expense import ExpenseORM

def init_db():
    Base.metadata.create_all(engine)
