class Book:
    def __init__(self, isbn, title, author, price) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__price = price
        
    @property
    def isbn(self):
        return str(self.__isbn)
    
    @property
    def title(self):
        return str(self.__title)

    def __str__(self) -> str:
        return f"Book isbn={self.__isbn}, title={self.__title}, author={self.__author}, price={self.__price}"
    
    def __repr__(self) -> str:
        return str(self)
    
class BookList:
    def __init__(self) -> None:
        self.__books: list[Book] = []

    def add_book(self, book):
        self.__books.append(book)

    def __str__(self) -> str:
        output = "The list of books\n"
        for book in self.__books:
            output += str(book) + "\n"
        return output
