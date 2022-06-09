import my_functions
import os

books = []
while(True):
    my_functions.print_options()
    user_input= input()
    if user_input == 'x' or user_input == 'X':
        break
    if user_input == "1":
        books.append(my_functions.create_book())
    elif user_input == "2":
        my_functions.save_books(books)
    elif user_input == "3":
        books = my_functions.load_books()
    elif user_input == "4":
        my_functions.issue_book(books)
    elif user_input == "5":
        my_functions.return_book(books)
    elif user_input == "6":
        my_functions.update_book(books)
    elif user_input == "7":
        my_functions.show_all_books(books)
    elif user_input == "8":
        my_functions.show_specific_book(books)
    else:
        continue
    
