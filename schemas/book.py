from datetime import date
from pydantic import BaseModel


class BookBase(BaseModel):
    id: str
    title: str
    description: str | None = None
    published_date: date | None = None
    page_count: int | None = None
    thumbnail: str | None = None
