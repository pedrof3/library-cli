from uuid import uuid4

class User:
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(uuid4())[:8]
        
    def to_dict(self):
        pass
    
    def from_dict(self):
        pass