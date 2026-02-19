class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def get_age(self):
        """Calculates the age of the book based on the year 2025."""
        current_year = 2025
        return current_year - self.year


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: int):
        # 1. Extend the constructor using super()
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        # 2. Override the __str__ method and append file size
        base_string = super().__str__()
        return f"{base_string} ({self.file_size} MB)"


if __name__ == '__main__':
    # Creating an instance of EBook
    my_ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 12)
    
    # Printing the EBook (Tests the overridden __str__)
    print(f"EBook Details: {my_ebook}")
    
    # Calling get_age (Tests inheritance from Book)
    print(f"This ebook is {my_ebook.get_age()} years old.")