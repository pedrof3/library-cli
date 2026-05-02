from database import JsonDB
from biblioteca import Librabry
from cli import Cli

def main():
    data = JsonDB()
    system = Librabry(data)
    interface = Cli(system)
    
    interface.main_menu()
    
if __name__ == "__main__":
    main()