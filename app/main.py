from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import books, book_reviews

app = FastAPI()

app.include_router(books.router)
app.include_router(book_reviews.router)

# TODO:ミドルウェア用のファイルに移行する
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
