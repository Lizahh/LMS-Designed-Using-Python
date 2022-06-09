# This class will have own attributes and two dict methods
# Attributes: id, name, description, isbn, page_count, issued, author, year
# Initialize these attributes in init method
# Add a method 'to_dict' that returns all these attributes in the form of a dictionary

class Book():
    def __init__(self, id, name, description, isbn, page_count, issued, author, year):
        self.id = id
        self.name = name
        self.description = description
        self.isbn = isbn
        self.page_count = page_count
        self.issued = issued
        self.author = author
        self.year = year

    def to_dict(self):
        dictionary = {"id": self.id, "Name": self.name, "Description": self.description, "ISBN": self.isbn, "Page Count": self.page_count, "issued": self.issued, "Author": self.author, "Year": self.year}
        return dictionary
