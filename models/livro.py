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
            "titulo": self.title,
            "autor": self.author,
            "lingua": self.language,
            "id": self.id,
            "disponivel": self.available
        }
    
    def from_dict(self, data: dict):
        return self(
            title=data["titulo"],
            author=data["autor"],
            language=data["lingua"],
            id=data["id"],
            available=data["disponivel"]
        )