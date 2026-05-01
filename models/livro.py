from uuid import uuid4

class Book:
    
    def __init__(self, title: str, author: str, language: str):
        self.title = title
        self.author = author
        self.language = language
        self.id = str(uuid4())[:8]
        self.available = True
        
    def to_dict(self):
        pass
    
    def from_dict(self):
        pass