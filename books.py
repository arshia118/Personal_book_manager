import json

def show_books(books):
    for book in books:
        print("Book Name:", book["book_name"], "-" "Priority:", book["book_priority"])

def save_books(books):
    with open("result.json", "w", encoding ="utf-8") as file:
        json.dump(books, file, ensure_ascii = False, indent =2 )

def load_books():
    try:
        with open("result.json", "r",encoding ="utf-8")as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return[]