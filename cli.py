from database import JsonDB
from models.emprestimo import Loan
from models.livro import Book
from models.usuario import User

class Cli:
    
    def __init__(self, library):
        self.library = library
    
    def main_menu(self) -> None:
        while True:
            print("""
=== SISTEMA BIBLIOTECA ===
1. ADICIONAR LIVRO
2. ADICIONAR USUÁRIO
3. EMPRESTAR LIVRO
4. DEVOLVER LIVRO
5. LISTAR LIVROS
6. LISTAR USUÁRIOS
7. FECHAR PROGRAMA
                  """)
            
            command = input()
            
            if command == "1":
                self.add_book()
            elif command == "2":
                self.add_user()
            elif command == "3":
                self.loan_book()
            elif command == "4":
                self.return_book()
            elif command == "5":
                self.get_books()
            elif command == "6":
                self.get_users()
            elif command == "7":
                exit()
            else:
                print("Comando inválido.")
                
    def add_book(self) -> None:
        print("=== ADICIONAR LIVRO ===")
        title = input("Título do livro: ")
        author = input("Autor do livro: ")
        language = input("Idioma do livro: ")
        
        new_book = Book(title, author, language)
        self.library.add_book(new_book)
    
    def add_user(self) -> None:
        print("=== ADICIONAR USUÁRIO ===")
        first_name = input("Primeiro nome: ")
        last_name = input("Sobrenome: ")
        
        new_user = User(first_name, last_name)
        self.library.add_user(new_user)

    def loan_book(self) -> None:
        print("=== EMPRESTAR LIVRO ===")
        id_book = input("ID do livro: ")
        id_user = input("ID do usuário: ")
    
        new_loan = Loan(id_book, id_user)

        if self.library.loan_book(new_loan):
            print("EMPRÉSTIMO REALIZADO COM SUCESSO.")
        else:
            print("O EMPRÉSTIMO NÃO PÔDE SER CONCLUÍDO.")

    def return_book(self) -> None:
        print("=== DEVOLVER LIVRO ===")
        id_loan = input("ID do empréstimo: ")

        if self.library.return_book(id_loan):
            print("DEVOLUÇÃO FEITA COM SUCESSO.")
        else:
            print("A DEVOLUÇÃO NÃO FOI CONCLUÍDA")

    def get_books(self) -> None:
        print("=== LIVROS LISTADOS ===")
        print(self.library.get_books())

    def get_users(self) -> None:
        print("=== USUÁRIOS LISTADOS ===")
        print(self.library.get_users())