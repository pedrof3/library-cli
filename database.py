import json
import pathlib

PATH_NAME = pathlib.Path() / "database"
FILE_NAME = PATH_NAME / "database.json"

class JsonDB:
    
    def __init__(self):
        self.path_name = PATH_NAME
        self.file_name = FILE_NAME
    
    def save_data(self, data: dict) -> None:
        try:
            with open(self.file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except:
            pass
    
    def load_data(self) -> dict:
        if not self.file_name.exists():
            self.path_name.mkdir(parents=True, exist_ok=True)
            self.file_name.touch(exist_ok=True)
            return self.save_data({"livros": {}, "usuários": {}, "empréstimos": {}})
        
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                return json.load(f)
            
        except FileNotFoundError:
            return self.save_data({"livros": {}, "usuários": {}, "empréstimos": {}})
        