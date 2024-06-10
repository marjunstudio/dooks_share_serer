from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.sql import func
from database.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(String(12), primary_key=True, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    published_date = Column(Date, nullable=True)
    page_count = Column(Integer, nullable=True)
    thumbnail = Column(String(200), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now())
