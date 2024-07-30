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
                        "id": book[0],
                        "title": book[1],
                        "author": book[2],
                        "genre": book[3],
                        "publication_year": book[4],
                        "rating": book[5],
                        "registry_date": book[6],
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