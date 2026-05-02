import json
import pathlib

PATH_NAME = pathlib.Path() / "database"
BOOKS_FILE = PATH_NAME / "books.json"
LOANS_FILE = PATH_NAME / "loans.json"
USERS_FILE = PATH_NAME / "users.json"

class JsonDB:
    
    def __init__(self):
        self.path_name = PATH_NAME
        self.books_file = BOOKS_FILE
        self.loans_file = LOANS_FILE
        self.users_file = USERS_FILE

    def save_book(self, data:dict) -> None:
        try:
            with open(self.books_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except:
            pass

    def load_book(self) -> list[dict]:
        if not self.books_file.exists():
            self.path_name.mkdir(parents=True, exist_ok=True)
            self.books_file.touch(exist_ok=True)
            return self.save_book([])
        
        try:
            with open(self.books_file, "r", encoding="utf-8") as f:
                return json.load(f)
            
        except FileNotFoundError:
            return self.save_book([])
    
    def save_loan(self, data:dict) -> None:
        try:
            with open(self.loans_file_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except:
            pass

    def load_loan(self) -> list[dict]:
        if not self.loans_file.exists():
            self.path_name.mkdir(parents=True, exist_ok=True)
            self.loans_file.touch(exist_ok=True)
            return self.save_loan([])
        
        try:
            with open(self.loans_file, "r", encoding="utf-8") as f:
                return json.load(f)
            
        except FileNotFoundError:
            return self.save_loans([])

    def save_user(self, data:dict) -> None:
        try:
            with open(self.users_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except:
            pass

    def load_user(self) -> list[dict]:
        if not self.users_file.exists():
            self.path_name.mkdir(parents=True, exist_ok=True)
            self.users_file.touch(exist_ok=True)
            return self.save_book([])
        
        try:
            with open(self.users_file, "r", encoding="utf-8") as f:
                return json.load(f)
            
        except FileNotFoundError:
            return self.save_user([])