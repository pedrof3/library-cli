from uuid import uuid4

class User():
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = uuid4()
        self.books = []
        
        def get_books(self) -> int:
            return self.books
            
        def get_name(self) -> str:
            return f"{self.first_name.title()} {self.last_name.title()}"