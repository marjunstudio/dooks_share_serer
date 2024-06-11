from fastapi import Depends
from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookBase

from app.dependencies import get_db


def get_book_by_id(book_id: str, db: Session = Depends(get_db)):
    book_data = db.query(Book).filter(Book.id == book_id).one_or_none()
    print(f"検索結果表示:{book_data}")
    return book_data


def create_book_repo(book: BookBase, db: Session = Depends(get_db)):
    print(f"{book.id}のデータを検索")
    book_data = db.query(Book).filter(Book.id == book.id).one_or_none()
    if book_data:
        print(f"書籍ID {book.id} は登録済みです")
        return {}

    try:
        print("保存処理を開始")
        db_book = Book(
            id=book.id,
            title=book.title,
            description=book.description,
            published_date=book.published_date,
            page_count=book.page_count,
            thumbnail=book.thumbnail,
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        print(f"Error occurred while creating book: {str(e)}")
        return {}
