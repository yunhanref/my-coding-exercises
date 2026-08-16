#aggregation: has-a relationship.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Kitapları tutacak liste

    def add_book(self, book):
        # Aggregation burada gerçekleşiyor:
        # Dışarıda oluşturulmuş nesne buraya aktarılıyor.
        self.books.append(book)

    def list_books(self):
        print(f"--- {self.name} Kütüphanesindeki Kitaplar ---")
        for book in self.books:
            print(f"- {book.title} ({book.author})")


# 1. Bağımsız Kitap nesnelerini oluşturuyoruz
b1 = Book("De Natura Deorum", "Cicero")
b2 = Book("İçimdeki Karanlık", "Orhan Yenen")

# 2. Kütüphane nesnesini oluşturuyoruz
my_library = Library("Milli Kütüphane")

# 3. Kitapları kütüphaneye ekliyoruz (Aggregation)
my_library.add_book(b1)
my_library.add_book(b2)

my_library.list_books()

# 4. Kütüphaneyi yok etsek bile kitaplar silinmez!
del my_library

# b1 nesnesi hala hafızada sapasağlam duruyor:
print(f"\nKütüphane silindi ama kitap duruyor: {b1.title}, {b2.title}")