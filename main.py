import sys

from books import *
from order import *
from commands import *
from invoker import Invoker


book1 = Book("147894840X", "The otherside of midnight", "Sidney Sheldon", "$9.5")
book2 = Book("0446350109", "Windmills of the gods", "Sidney Sheldon", "$8")
book3 = Book("0307474275", "The Da Vinvi's code", "Dan Brown", "$21")

books_dict = {"1": book1, "2": book2, "3": book3}

order_class = Order()
book_list_class = BookList()

def main():
    user_order = process_order()
    order = user_order[1]
    book_list = user_order[0]
    
    user_input = input("""
                Would you like to add another book?
                1. Yes
                2. No
                """)
    
    while True:
        if user_input == "1":
            user_order = process_order()
        
            order = user_order[1]
            book_list = user_order[0]
            
            user_input = input("""
                       Would you like to add another book?
                       1. Yes
                       2. No
                       """)
        else:
            break
        
    user_input = input("""
                    Would you like to submit order?
                    1. Yes(Proceed)
                    2. No(Cancel order)
                    """)
    
    # process user order
    if user_input == "1":
        submit_order = Invoker()
        submit_order.command(SubmitOrderCommand(order, book_list))
        invoice = submit_order.execute()
        
        display_invoice = Invoker()
        display_invoice.command(DisplayInvoiceCommand(invoice))
        actual_invoice = display_invoice.execute()
        
        print(actual_invoice)
    
    # cancel user order
    elif user_input == "2":
        print("Order cancelled.")

def take_order():
    """script to take user order."""
    user_input = input(f"""
                Please select a book with exact number\n
                1. {book1.title}\n
                2. {book2.title}\n
                3. {book3.title}\n
                """)
    
    quantity = int(input("Please input the quantity in number."))
    
    return [user_input, quantity]

def process_order():
    user_order = take_order()
    try:
        book = books_dict[user_order[0]]
    except KeyError as e:
        print(f"Please input a valid number. {e} is not valid")
        sys.exit()
        
    add_book = Invoker()
    add_book.command(AddToBooklistCommand(book, book_list_class))
    book_list = add_book.execute()
    
    add_order = Invoker()
    add_order.command(AddOrderItemCommand(book.isbn, user_order[1], order_class))
    order = add_order.execute()
    
    return [book_list, order]            
            
if __name__ == "__main__":
    main()
