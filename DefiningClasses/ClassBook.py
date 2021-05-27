from dataclasses import dataclass

@dataclass
class Book:
    name:str
    author:str
    pages:int

book=Book("Igor","Ruzha",1)
print(book.name)

    # sled versia 2.3.7
