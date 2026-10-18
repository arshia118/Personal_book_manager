from books import show_books, save_books, load_books
import os
from dotenv import load_dotenv 


name = input("enter your name :")

load_dotenv()

admin_password = os.getenv("BOOK_MANAGER_PASSWORD")

admin = input("do you want to go to admin mod y/n ?")
if admin == "y":
    while True:
        input_addmin_pass = input("enter the  pass word to exit type exit  :")
        if input_addmin_pass == admin_password:
            print("admin mod on")
            break
        else:
            print("wrong password")
            continue


print("welcome", name)

books = load_books()
number = int(input("how many books do you want to add ?"))

for i in range(number):
    book = input("enter a book name :")
    books.append(book)

show_books(books)
save_books(books)




