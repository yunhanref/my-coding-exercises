#aggregation: has-a relationship.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"--- {self.name} Kütüphanesindeki Kitaplar ---")
        for book in self.books:
            print(f"- {book.title} ({book.author})")


b1 = Book("De Natura Deorum", "Cicero")
b2 = Book("İçimdeki Karanlık", "Orhan Yenen")

my_library = Library("Milli Kütüphane")

my_library.add_book(b1)
my_library.add_book(b2)

my_library.list_books()

del my_library

print(f"\nKütüphane silindi ama kitap duruyor: {b1.title}, {b2.title}")
