from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database.database import SessionLocal
from schemas.book_review import BookReviewBase
from schemas.book import BookBase

from app.repository.book_repo import create_book_repo
from app.repository.book_review_repo import create_book_review_repo

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/book_reviews", tags=["レビュー投稿"], summary="書籍のレビューを投稿する")
def create_book_review(book: BookBase, book_review: BookReviewBase, db: Session = Depends(get_db)):
    try:
        book_data = create_book_repo(db=db, book=book)
        review_data = create_book_review_repo(db=db, review=book_review)
        return book_data, review_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error occurred: {str(e)}")
