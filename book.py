from uuid import uuid4

class Book():
    
    def __init__(self, name: str, category: str, pages: int, author: str, language: str):
        self.name = name
        self.category = category
        self.pages = pages
        self.author = author
        self.language = language
        self.book_id = uuid4()
        self.available = True
        
    
    