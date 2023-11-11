class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}\n")


class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_inventory(self):
        if not self.books:
            print("No books in inventory yet.")
        else:
            print("Current Inventory:")
            for book in self.books:
                book.display_info()
    
    def total_books(self):
        count = 0
        for book in self.books:
            count += book.quantity
        return count
    
    def total_cost(self):
        price = 0
        for book in self.books:
            price += book.price
        return price
    



# Create instances of the Book class
book1 = Book("Python 101", "John Smith", "Programming", 25, 10)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 15, 20)

# Create an instance of the Bookstore class
bookstore = Bookstore()

# Add books to the bookstore inventory
bookstore.add_book(book1)
bookstore.add_book(book2)

# Display the inventory
bookstore.display_inventory()
