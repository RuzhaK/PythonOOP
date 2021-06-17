class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book


one = Book("a", "b")
done = Book("c", "d")
library = Library([one, done])
print(library.find_book("a"))
