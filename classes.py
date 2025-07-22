class Smartphone:
    def __init__(self, brand, model, storage): # Class constructor
        self.brand = brand # Initializes brand
        self.model = model # Initializes model
        self.storage = storage # Initializes storage

    def display_info(self): # Method to display smartphone info
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Creating two objects
my_phone = Smartphone("Apple", "iPhone 13", 128)
your_phone = Smartphone("Samsung", "Galaxy S22", 256)

# Using a method to display info about the phones
my_phone.display_info()  # Outputs -> Smartphone: Apple iPhone 13, Storage: 128GB
your_phone.display_info() # Outputs -> Smartphone: Samsung Galaxy S22, Storage: 256GB

class Book:
    def __init__(self, title = "Animal Farm", author = "George Orwell", year = "1945"):
        self.title = title # Initializes title
        self.author = author # Initializes author
        self.year = year # Initializes year
    # Creating a method
    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
    def is_classic(self):
        if self.year < 1970:
            return True
        return False
    def __str__(self):
        return str(self.__dict__)

book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book1.describe()
print(book1.is_classic())
print(book1)
book2 = Book()
print(book2)