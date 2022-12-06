from abc import ABC, abstractmethod

from books import *
from order import *
from invoice import Invoice


class Command(ABC):
    @abstractmethod
    def process(self):
        pass

class DisplayBookListCommand(Command):
    def __init__(self, booklist: BookList):
        self.__booklist = booklist
        
    def process(self) -> str:
        return str(self.__booklist)
    
class AddOrderItemCommand(Command):
    def __init__(self, isbn, quantity, order: Order):
        self.__isbn = isbn
        self.__quantity = quantity
        self.order = order
        
    def process(self) -> Order:
        self.order.add_item(self.__isbn, self.__quantity)
        return self.order
    
class RemoveOrderItem(Command):
    def __init__(self, isbn):
        self.__isbn = isbn

    def process(self) -> Order:
        return Order().remove_item(self.__isbn)
    
class DisplayOrderCommand(Command):
    def __init__(self, order: Order):
        self.__order = order
    
    def process(self):
        return str(self.__order)

class SubmitOrderCommand(Command):
    def __init__(self, order: Order, booklist: BookList):
        self.__order = order
        self.__booklist = booklist
        
    def process(self):
        return Invoice(self.__order, self.__booklist)

class DisplayInvoiceCommand(Command):
    def __init__(self, invoice: Invoice):
        self.__invoice = invoice
        
    def process(self) -> str:
        return str(self.__invoice)

class AddToBooklistCommand(Command):
    def __init__(self, book, book_list: BookList):
        self.__book = book
        self.book_list = book_list
        
    def process(self) -> BookList:
        self.book_list.add_book(self.__book)
        return self.book_list
