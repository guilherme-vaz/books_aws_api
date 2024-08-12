# import boto3
from typing import Dict, List
from src.models.settings.db_connection_handler import table

class Book:
    def __init__(self) -> None:
        self.__table = table
    
    def registry_book(self, book_infos: Dict) -> None:
        self.__table.put_item(Item=book_infos)
    
    def find_book(self, book_id: str) -> Dict:
        self.__table.get_item(Key={'id': book_id})
    
    def get_all_books(self) -> List[Dict]:
        self.__table.scan()