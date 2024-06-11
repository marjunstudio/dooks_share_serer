from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.sql import func
from database.database import Base


class BookReview(Base):
    __tablename__ = "book_reviews"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String(100), nullable=False)
    book_id = Column(String(12), ForeignKey("books.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now())
