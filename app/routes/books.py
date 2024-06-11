from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookBase

from app.dependencies import get_db

router = APIRouter()

#TODO:おそらく使用しないエンドポイントなので削除予定
# def get_book_by_id(book_id: str, db: Session = Depends(get_db)):
#     book_data = db.query(Book).filter(Book.id == book_id).one_or_none()
#     return book_data


# @router.post("/books")
# def create_book(book: BookBase, db: Session = Depends(get_db)):
#     book_data = get_book_by_id(book.id, db)
#     if book_data:
#         raise HTTPException(status_code=400, detail="Book already registered")

#     try:
#         print("保存処理を開始")
#         db_book = Book(
#             id=book.id,
#             title=book.title,
#             description=book.description,
#             published_date=book.published_date,
#             page_count=book.page_count,
#             thumbnail=book.thumbnail,
#         )
#         db.add(db_book)
#         db.commit()
#         db.refresh(db_book)
#         return db_book
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Unexpected error occurred: {str(e)}")
