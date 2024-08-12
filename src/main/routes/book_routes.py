import json
from src.controllers.BooksControllers.book_registry import BookRegistry
from src.controllers.BooksControllers.get_all_books import GetAllBooks
from src.controllers.BooksControllers.book_finder import BookFinder

def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    path = event.get('path')
    
    if http_method == 'POST' and path == '/books':
        return BookRegistry.registry(event)
    elif http_method == 'GET' and path == '/books':
        return GetAllBooks.get_all_books()
    elif http_method == 'GET' and '/books/' in path:
        book_id = path.split('/')[-1]
        return BookFinder.find_book(book_id)
    else:
        return {
            'body': json.dumps("Route not found :("),
            'satusCode': 404
        }

