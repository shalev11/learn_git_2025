import json

with open("books.json",'r') as f:
    book_list = json.load(f)

    for book in book_list:
        print(f"book_Title:{book['Title']}")
        print(f"book_Author:{book['Author']}")