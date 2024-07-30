# import boto3
from typing import Dict, List, Tuple
from mysql.connector import MySQLConnection

class Book:
    def __init__(self, conn: MySQLConnection) -> None:
        self.__conn = conn
    
    def registry_book(self, book_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO books
                    (id, title, author, genre, publication_year, rating, registry_date)
                VALUES
                    (?, ? , ?, ?, ?, ?, ?)
            ''',(
                book_infos["id"],
                book_infos["title"],
                book_infos["author"],
                book_infos["genre"],
                book_infos["publication_year"],
                book_infos["rating"],
                book_infos["registry_date"],
            )
        )
        self.__conn.commit()
    
    def find_book(self, book_id: str) -> Dict:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM books WHERE book_id = ?
            ''', (book_id,)
        )
        
        book = cursor.fetchone()
        return book
    
    def get_all_books(self) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM books
            '''
        )
        
        books = cursor.fetchall()
        return books
    