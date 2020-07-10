from book import Book
import json


class Search:

    def Search(self):
        bookDatabase = open("booksset.json", "w")
        bookDatabase = json.dumps(bookDatabase)
        searchType = input("""do you want to search via:
        - title
        - author
        - ISBN
        Type the word for the search key
        """)
        searchType.lower()

        if (searchType == "title"):
            searchKey = input("Enter the title:> ")
            for i in bookDatabase["title"]:
                if (bookDatabase["title"] == searchKey):
                    print("this book is at our library")
                else:
                    print("We do not have this book")

        if (searchType == "author"):
            searchKey = input("Enter the author:> ")
            for i in bookDatabase["author"]:
                if (bookDatabase["author"] == searchKey):
                    print("I don't know what to do here")

        if (searchType == "isbn"):
            searchKey = input("Enter the ISBN:> ")
            for i in bookDatabase["isbn"]:
                if (bookDatabase["isbn"] == searchKey):
                    print("This book is in our library")
                else:
                    print("We do not have this book in our library")