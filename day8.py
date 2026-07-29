#create a class called LibraryBook

class LibraryBook:
    #create a constructor that takes in the title, author, and ISBN number of the book
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True  # Add an attribute to track availability

    #create a method called borrow, displaing a messag that the book has been borrowed
    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is not available for borrowing.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Year: {self.year}")

book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
book2 = LibraryBook("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960)
book3 = LibraryBook("The Great Well", "George Orwell", "9780451524935", 1949)

book1.display_details()
book1.borrow()
book1.display_details()
book1.return_book()
book1.display_details()

book2.display_details()
book2.borrow()
book2.display_details()
book2.return_book()
book2.display_details()

book3.display_details()
book3.borrow()
book3.display_details()
book3.return_book()
book3.display_details()


