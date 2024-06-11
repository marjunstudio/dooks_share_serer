from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.book_review import BookReview
from schemas.book_review import BookReviewBase


def create_book_review_repo(db: Session, review: BookReviewBase):
    try:
        print("レビューの保存処理を開始")
        review_data = BookReview(
            content=review.content,
            book_id=review.book_id,
        )
        db.add(review_data)
        db.commit()
        db.refresh(review_data)
        return review_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error occurred: {str(e)}")
