class OrderItem:
    def __init__(self, isbn, quantity) -> None:
        self.isbn = isbn
        self.quantity = quantity
        
    def __str__(self) -> str:
        return f"Order item isbn={self.isbn}, quantity={self.quantity}"
    
    def __repr__(self) -> str:
        return str(self)

class Order:
    def __init__(self) -> None:
        self.__orderitems: list[OrderItem] = []

    def add_item(self, isbn, quantity):
        self.__orderitems.append(OrderItem(isbn, quantity))
        
    def remove_item(self, isbn):
        for order in self.__orderitems:
            if order.isbn == isbn:
                self.__orderitems.pop(self.__orderitems.index(order))
        return f"{isbn} removed from order items."
        
    def __str__(self) -> str:
        output = "The list of order items\n"
        for items in self.__orderitems:
            output += str(items) + "\n"
        return output
