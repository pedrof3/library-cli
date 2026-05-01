from uuid import uuid4

class Book:
    
    def __init__(self, title: str, author: str, language: str):
        self.title = title
        self.author = author
        self.language = language
        self.id = str(uuid4())[:8]
        self.available = True
        
    def to_dict(self) -> dict:
        return {
            "título": self.title,
            "autor": self.author,
            "língua": self.language,
            "id": self.id,
            "disponível": self.available
        }
    
    def from_dict(self, data: dict):
        return self(
            title=data["título"],
            author=data["autor"],
            language=data["língua"],
            id=data["id"],
            available=data["disponível"]
        )