# Build a `Library` class. Attributes: name, list of books (each book: title, author, available). Methods: `add_book`, `remove_book`, `checkout(title)`, `return_book(title)`, `search(query)` — matches title or author, `available_books()`, `report()` — full summary. Create a library, add 5 books, checkout one, return it, search for something, print the report.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, available = True):
        booksDict = {
            "title": title,
            "author": author,
            "available": available
        }
        self.books.append(booksDict)

    def remove_book(self, title):
        found = False
        for index, book in enumerate(self.books):
            if book["title"] == title:
                self.books.pop(index)
                print(f"Book {title} is removed.")
                found = True
                break
        if not found:
            print(f"There is no book titled {title} in library")

    def checkout(self, title):
        found = False
        for book in self.books:
            if book["title"] == title:
                book["available"] = False
                print(f"Book {title} checked out successfully.")
                found = True
                break
        if not found:
            print(f"Book {title} not found.")

    def return_book(self, title):
        found = False
        for book in self.books:
            if book["title"] == title:
                book["available"] = True
                print(f"Book {title} returned successfully.")
                found = True
                break
        if not found:
            print(f"Book {title} is not from this library.")

    def search(self, query):
        results = [book for book in self.books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
        return results

    def available_books(self):
        return [book for book in self.books if book["available"]]
            
    def report(self):
        print(f"Library Name: {self.name}")
        print(f"Total books in library: {len(self.books)}")
        print("Books currently available:")
        for book in self.books:
            if book["available"] == True:
                print(f"\tBook name: {book['title']}\n\tBook's Author: {book['author']}\n")

        print("Books already Checked out:")
        for book in self.books:
            if book["available"] == False:
                print(f"\tBook name: {book['title']}\n\tBook's Author: {book['author']}\n")

        print("List of all books with their current availability:")
        for book in self.books:
            print(f"\tBook name: {book['title']}\n\tBook's Author: {book['author']}\n\tAvailable: {book['available']}\n")

lib1 = Library("Best Lib")
lib1.add_book("The Hobbit", "J.R.R. Tolkien")
lib1.add_book("1984", "George Orwell")
lib1.add_book("To Kill a Mockingbird", "Harper Lee")
lib1.add_book("The Great Gatsby", "F. Scott Fitzgerald")
lib1.add_book("Pride and Prejudice", "Jane Austen")

lib1.checkout("1984")
lib1.return_book("1984")

results = lib1.search("Orwell")
print(results)

lib1.report()