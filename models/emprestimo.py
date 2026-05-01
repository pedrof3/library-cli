from uuid import uuid4
from datetime import datetime

class Loan:
    
    def __init__(self, book_id: str, user_id: str):
        self.book_id = book_id
        self.user_id = user_id
        self.id = str(uuid4())[:8]
        self.loan_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    def to_dict(self):
        pass
    
    def from_dict(self):
        pass
    