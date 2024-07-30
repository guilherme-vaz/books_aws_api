from typing import Dict

class BookFinder:
    def __init__(self, books_repository) -> None:
        self.__books_repository = books_repository
        
    def find_book(self, bookId) -> Dict:
        try:
            book = self.__books_repository.find__book(bookId)
            if not book: raise Exception("No book found")
            return {
                "body": {
                    "book": {
                        "id": book[0],
                        "title": book[1],
                        "author": book[2],
                        "genre": book[3],
                        "publication_year": book[4],
                        "rating": book[5],
                        "registry_date": book[6],
                    }
                }, "status_code": 200
            }
            
        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }