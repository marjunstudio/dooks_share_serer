from fastapi import FastAPI
from app.routes import books, book_reviews

app = FastAPI()

app.include_router(books.router)
app.include_router(book_reviews.router)
