from pydantic import BaseModel


class BookReviewBase(BaseModel):
    content: str
    book_id: str
