from typing import Dict, List

class GetAllBooks:
    def __init__(self, books_repository) -> None:
        self.__books_repository = books_repository
    
    def get_all_books(self) -> List[Dict]:
        try:
            books = self.__books_repository.get_all_books()
            formatted_books = []
            
            for book in books:
                formatted_books.append({
                    "id": book.get("id"),
                    "title": book.get("title"),
                    "author": book.get("author"),
                    "genre": book.get("genre"),
                    "publication_year": book.get("publication_year"),
                    "rating": book.get("rating"),
                    "registry_date": book.get("registry_date"),
                })
                
            return {
                "body": { "books": formatted_books },
                "status_code": 200
            }
                
        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }