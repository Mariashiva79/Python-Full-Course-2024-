# Magic Methods, son métodos con __ __ para acceder a los datos de la
#                clase: __init__, __str__, __eq__, etc.

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):  # este hace que se imprima el string y no el código que sale de normal
        return f"{self.title} by {self.author}"

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages in total"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): # tiene más páginas el otro
        return self.num_pages < other.num_pages

    def __gt__(self, other): # tiene menos páginas el otro
        return self.num_pages > other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' is not in this book"


book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("1984", "George Orwell", 328)
book4 = Book("Pride and Prejudice", "Jane Austen", 432)
book5 = Book("Don Quixote", "Miguel de Cervantes", 863)

print(book5 + book1)
print(book4 == book2)
print(book5 < book1)
print(book5 > book1)
print("Don" in book3)
print(book4["title"])