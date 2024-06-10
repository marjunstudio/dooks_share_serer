from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.book import Book
from schemas.book import BookBase

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_book_by_id(book_id: str, db: Session = Depends(get_db)):
    book_data = db.query(Book).filter(Book.id == book_id).one_or_none()
    return book_data


@app.post("/books")
def create_book(book: BookBase, db: Session = Depends(get_db)):
    book_data = get_book_by_id(book.id, db)
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
