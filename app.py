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
        print("book is saved ...")
    elif user_input == "3":
        books = my_functions.load_books()
    elif user_input == "4":
        print(my_functions.find_book(books, "4234"))
    else:
        continue
        # everytime clear the screen to show the print_options() function's menu 
    #os.system('cls')
    
