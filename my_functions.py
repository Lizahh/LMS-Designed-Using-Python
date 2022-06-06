from operator import index
import book
import json

def print_options():
    print("Press the specific button for that action:\n")
    print("1-Create a new book")
    print("2-Save books Locally")
    print("3-Load books from the disk")
    print("4-Issue book")
    print("5-Return a book")
    print("6-Update a book")
    print("7-Show all books")
    print("8-Show books")
    print("\nYour Option:")

def book_info():
    # this is the information that we need: id, name, description, isbn, page_count, issued, author, year
    issued = False
    page_count = False
    year = False
    bookid = False
    while(bookid == False):
        create_id = input("Please enter the book ID: ")
        if create_id.isnumeric():
            create_id = int(create_id)
            bookid = True
        else:
            print("\n\tHi, Please enter book ID in \"Numbers\". You entered in \"Text\" which is wrong!!!\n")
            bookid = False
    
    create_name = input("Please enter the book name: ")
    create_description = input("Please enter the book description: ")
    create_isbn = input("Please enter the book ISBN: (Use dashes '-' if you need) ")
    while(page_count == False):
        create_page_count = input("Please enter the book's total number of pages: ")
        if create_page_count.isnumeric():
            create_page_count = int(create_page_count)
            page_count = True
        else:
            print("\n\tHi, Please enter number of pages in \"Numbers\". You entered in \"Text\" which is wrong!!!\n")
            page_count = False
    while(issued == False):
        create_issued = input("Please enter if the book is issued or not: \"Y\" or \"y\" for yes & \"N\" or \"n\" for No: ")
        if create_issued.lower() == "y" or create_issued.lower() == "n":
            issued = True
        else:
            print("\n\tHi! You didn't input the right character for issued book. Please re-enter \"Y\" or \"y\" for yes & \"N\" or \"n\" for No !!!\n")
            issued = False
    create_author = input("Please enter the name of the author of book : ")
    while(year == False):
        create_year = input("Please enter the year of book: ")
        if create_year.isnumeric():
            create_year = int(create_year)
            year = True
        else:
            print("\n\tHi, Please enter year in \"Numbers\". You entered in \"Text\" which is wrong!!!\n")
            year = False
    return {"id": create_id, "Name": create_name, "Description": create_description, "ISBN": create_isbn, "Page Count": create_page_count, "Issued": create_issued, "Author": create_author, "Year": create_year}

def create_book():
    print("Please provide the following information to create a new book:")
    new_created_book = book_info()
    booked_book = book.Book(new_created_book["id"],new_created_book["Name"], new_created_book["Description"], new_created_book["ISBN"], new_created_book["Page Count"], new_created_book["Issued"], new_created_book["Author"], new_created_book["Year"])
    print(booked_book.to_dict())
    return booked_book


def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    
    try:
        file = open("books.dat", "w")
        file.write(json.dumps(json_books, indent = 4))
    
    except:
        print("There's an error in saving the books!!!")

def load_books():
    try:
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for each_book in loaded_books:
            new_obj = book.Book(each_book["id"],each_book["Name"], each_book["Description"], each_book["ISBN"], each_book["Page Count"], each_book["Issued"], each_book["Author"], each_book["Year"])
            books.append(new_obj)
        print("Books loaded successfully ... ")
        return books
    except:
        print("The file doesn't exist or some error occured while loading the file!!!")

def find_book(books, id):
    for index, each_book in enumerate(books):
        if each_book.id == id:
            return index
    return None
