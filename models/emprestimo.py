from uuid import uuid4
from datetime import datetime

class Loan:
    
    def __init__(self, book_id: str, user_id: str):
        self.book_id = book_id
        self.user_id = user_id
        self.id = str(uuid4())[:8]
        self.loan_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    def to_dict(self) -> dict:
        return {
            "id livro": self.book_id,
            "id usuario": self.user_id,
            "id emprestimo": self.id,
            "data emprestimo": self.loan_date
        }
    
    def from_dict(self, data: dict):
        return self(
            book_id=data["id livro"],
            user_id=data["id usuario"],
            id=data["id emprestimo"],
            loan_date=["data emprestimo"]
        )
    