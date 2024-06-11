from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookBase


def get_book_by_id(book_id: str, db: Session):
    book_data = db.query(Book).filter(Book.id == book_id).one_or_none()
    print(f"検索結果表示:{book_data}")
    return book_data


def create_book_repo(book: BookBase, db: Session):
    print(f"{book.id}のデータを検索")
    book_data = db.query(Book).filter(Book.id == book.id).one_or_none()
    if book_data:
        raise HTTPException(status_code=400, detail="Book already registered")

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
        raise HTTPException(status_code=500, detail=f"Unexpected error occurred: {str(e)}")
