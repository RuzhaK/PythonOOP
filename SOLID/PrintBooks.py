from abc import ABC,abstractmethod

class Book:
    def __init__(self,title,author,content:str):
        self.author = author
        self.content = content
        self.title = title

class Formatter(ABC):
    @abstractmethod
    def format(self,book:Book):
        return book.content

class ContentFormatter(Formatter):
    def format(self,book:Book):
        return book.content

class AuthorFormatter(Formatter):
    def format(self,book:Book):
        return book.author

class Printer:
    def print(self,book:Book,formatter:Formatter):

        return formatter.format(book)

book=Book('Principles','Ray Dalio',' Ala bala')
printer=Printer()
print(printer.print(book,AuthorFormatter()))
