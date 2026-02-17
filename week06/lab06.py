class Book:
    def __init__(self, title, author, year):
        # Store the parameters as instance attributes
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'

    def get_age(self):
        return 2025 - self.year

class EBook(Book):  # EBook inherits from Book
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)  # Call parent constructor
        self.file_size = file_size  # Add new attribute

    def __str__(self):
        # Get the parent's string representation
        parent_str = super().__str__()
        # Add our own information
        return f"{parent_str} ({self.file_size} MB)"

if __name__ == '__main__':
    # test my work
    my_book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(my_book)

    my_ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(my_ebook)
    print(my_ebook.get_age())
