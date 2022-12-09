from books import *
from order import *

class Invoice:
    def __init__(self, order: Order, booklist: BookList) -> None:
        self.__order = order
        self.__booklist = booklist
        
    def __str__(self) -> str:
        output = f"Invoice\n"
        output += f"{self.__order}\n"
        output += f"{self.__booklist}\n"
        return output
