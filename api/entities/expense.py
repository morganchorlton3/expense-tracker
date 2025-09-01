from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from api.db.base import Base

class ExpenseORM(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    account_id: Mapped[str] = mapped_column(String(64), index=True)
    posted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    amount_minor: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(String(3), default="GBP")
    payee: Mapped[str | None] = mapped_column(String(255), default=None)
    category: Mapped[str | None] = mapped_column(String(64), index=True, default=None)
    notes: Mapped[str | None] = mapped_column(String(500), default=None)
