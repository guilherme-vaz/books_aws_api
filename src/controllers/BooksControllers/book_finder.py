from typing import Dict
import json

class BookFinder:
    def __init__(self, books_repository) -> None:
        self.__books_repository = books_repository
        
    def find_book(self, bookId) -> Dict:
        try:
            response = self.__books_repository.find__book(bookId)
            book = response.get('Item', {})
            
            if not book: raise Exception("No book found")
            return {
                "body": json.dumps(book),
                "status_code": 200
            }
            
        except Exception as exception:
            return {
                "body": json.dumps({ "error": "Bad request", "message": str(exception)}),
                "status_code": 400
            }