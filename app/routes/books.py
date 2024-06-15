from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()


class BookRequest(BaseModel):
    title: str


@router.post("/v1/books", tags=["books"], summary="GoogleBooksAPIを使用して、書籍情報を取得する")
def get_books_info(book: BookRequest):
    url = (f"https://www.googleapis.com/books/v1/volumes?q={book.title}&key=AIzaSyCixJ4hHo0Mz6Wx8Z1DRFVnHjM8M0dTJN0&maxResults=10")
    print(url)
    results = requests.get(url)

    print(results.json())

    return results.json()
