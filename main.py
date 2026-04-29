from pathlib import Path
import json

DATA_FILE = Path.absolute() / "library.json"

def load_data():
    if not DATA_FILE.exists():
        return {"books": {}, "users": {}}
    try:
        with open("teste.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        pass
    
def save_data(data: dict) -> None:
    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
        
"""
    add book(infos)
    remove book(book_id)
    loan book(book_id, user_id)
    return book(book_id, user_id)
    list books()
    
    add user(infos)
    remove book(book_id)
    
"""

while True:
    req = input()