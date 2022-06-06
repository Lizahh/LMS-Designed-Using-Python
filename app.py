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
    if user_input == "2":
        my_functions.save_books(books)
        print("book is saved ...")
    else:
        continue
        # everytime clear the screen to show the print_options() function's menu 
    #os.system('cls')
    
