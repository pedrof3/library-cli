from database import JsonDB
from models.emprestimo import Loan
from models.livro import Book
from models.usuario import User

class Librabry:
    
    def __init__(self, data: JsonDB):
        self.data = JsonDB()

        self.books = [x for x in self.data.load_book()]
        self.loans = [y for y in self.data.load_loan()]
        self.users = [z for z in self.data.load_user()]
    
    def add_book(self, book: Book) -> None:
        self.books.append(book.to_dict())
        self.data.save_book(self.books)
    
    def get_books(self) -> str:
        output = ""
        for book in self.books:
            output += f"ID: {book["id"]}, Livro: {book["titulo"]}, Autor: {book["autor"]}, Língua: {book["lingua"]}\n"

        return output
    
    def loan_book(self, loan: Loan) -> bool:
        if loan.user_id not in [z["id"] for z in self.users]:
            return False
        
        if loan.book_id not in [x["id"] for x in self.books]:
            return False
        
        for book in self.books:
            if book["id"] == loan.book_id:
                if book["disponivel"] == False:
                    return False
                else:
                    book["disponivel"] = False
                    self.data.save_book(self.books)
        
        self.loans.append(loan.to_dict())
        self.data.save_loan(self.loans)

        return True
    
    def return_book(self, id_loan) -> bool:
        if id_loan not in [x["id emprestimo"] for x in self.loans]:
            return False
        
        idx = 0
        for loan in self.loans:
            if loan["id emprestimo"] == id_loan:
                for book in self.books:
                    if book["id"] == loan["id livro"]:
                        book["disponivel"] = True
                        self.data.save_book(self.books)
                break
            idx += 1

        del self.loans[idx]
        self.data.save_loan(self.loans)
    
    def add_user(self, user: User) -> None:
        self.users.append(user.to_dict())
        self.data.save_user(self.users)
    
    def get_users(self) -> str:
        output = ""
        for user in self.users:
            output += f"ID: {user["id"]}, Nome: {user["nome"]}, Sobrenome: {user["sobrenome"]}\n"

        return output
