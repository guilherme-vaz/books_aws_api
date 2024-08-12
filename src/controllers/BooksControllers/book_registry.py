import uuid
import json
from datetime import datetime
from typing import Dict
from src.models.repositories.book_repository import Book

class BookRegistry:
    def __init__(self, books_repository: Book) -> None:
        self.__books_repository = books_repository
    
    def registry(self, body) -> Dict:
        try:
            id = str(uuid.uuid4())
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
            
            bookData = json.loads(body.get('body'))
            
            book_infos = {
                'id': id,
                'title': bookData.get('title'),
                'author': bookData.get('author'),
                'genre': bookData.get('genre'),
                'publication_year': bookData.get('publication_year'),
                'rating': bookData.get('rating'),
                'registry_date': formatted_date
            }
            
            self.__books_repository.registry_book(book_infos)
            
            return {
                "body": json.dumps({ "bookId": id }),
                "status_code": 201    
            }
            
        except Exception as exception:
            return {
                "body": json.dumps ({ "error": "Bad request", "message": str(exception) }),
                "status_code": 400
            }