import uuid
from datetime import datetime
from typing import Dict


class BookRegistry:
    def __init__(self, books_repository) -> None:
        self.__books_repository = books_repository
    
    def registry(self, body) -> Dict:
        try:
            id = str(uuid.uuid4())
            now = datetime.now()
            fomatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
            book_infos = {
                "id": id,
                "title": body["title"],
                "author": body["author"],
                "genre": body["genre"],
                "publication_year": body["publication_year"],
                "rating": body["rating"],
                "registry_date":fomatted_date
            }
            
            self.__books_repository.registry_book(book_infos)
            
            return {
                "body": { "bookId": id },
                "status_code": 201    
            }
            
        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }