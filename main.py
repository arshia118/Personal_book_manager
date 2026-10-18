from books import show_books

name = input("enter your name :")

print("welcome", name)

books = []
number = int(input("how many books do you want to add ?"))

for i in range(number):
    book = input("enter a book name :")
    books.append(book)

show_books(books)




