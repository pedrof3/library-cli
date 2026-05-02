from database import JsonDB
from models.emprestimo import Loan
from models.livro import Book
from models.usuario import User

class Librabry:
    
    def __init__(self, data: JsonDB):
        self.data = JsonDB()

        self.books = [Book.from_dict(x) for x in self.data.load_data()]
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def get_books(self):
        pass
    
    def loan_book(self) -> bool:
        pass
    
    def add_user(self, user: User) -> None:
        pass
    
    def get_users(self):
        pass
