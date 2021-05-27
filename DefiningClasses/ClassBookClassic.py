class Book:
    def __init__(self,name: str,author: str,pages:int):
        self.name=name
        self.author=author
        self.pages=pages

book=Book("Igor","Ruzha",1)
print(book.name)