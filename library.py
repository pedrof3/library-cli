from book import Book
from user import User

class Library():
    
    def __init__(self, name:str):
        self.name = name
        self.books_available = 0
        pass
    
    def add_book(self, name: str, category: str, pages: int, author: str, language: str):
        new_book = Book(name, category, pages, author, language)
        
        with open("library.json", "w", encoding="utf-8") as f:
            pass
    
    def remove_book(self, id):
        pass
    
    def add_user(self, first_name: str, last_name: str):
        new_user = User(first_name, last_name)
        
        with open("library.json", "w", encoding="utf-8") as f:
            pass
    
    def remove_user(self, id):
        pass