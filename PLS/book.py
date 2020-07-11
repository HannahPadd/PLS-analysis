import json
import csv

class Book:
    def __init__(self, author, country, imageLink, language, link, pages, title, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year
        self.available = True
        

    def ReturnBook(self, Book, User):
        with open("Books.csv", "rt", newline='') as ReadFile:
            lines = list(csv.reader(ReadFile))

        with open("Books.csv", "wt", newline='') as WriteFile:
            done = False
            Writer = csv.writer(WriteFile)
            for row in lines:
                if row[0] == Book and row[2] == User.lower():
                    if done == False:
                        row[2] = None
                        done = True
                        Writer.writerow(row)
                    else:
                        Writer.writerow(row)
                else:
                    Writer.writerow(row)
    
    def LendBook(self, Book, User):
        with open("Books.csv", "rt", newline='') as ReadFile:
            lines = list(csv.reader(ReadFile))

        with open("Books.csv", "wt", newline='') as WriteFile:
            done = False
            Writer = csv.writer(WriteFile)
            for row in lines:
                if row[0] == Book and row[2] == "":
                    if done == False:
                        row[2] = User.lower()
                        done = True
                        Writer.writerow(row)
                    else:
                        Writer.writerow(row)
                else:
                    Writer.writerow(row)
                
    def SaveBook(self):
        saveBook = json.dumps(self.__dict__)
        database = open("bookDatabase.json", "r+")
        try:
            data = json.loads(database)
            data.update(saveBook)
            data = json.dumps(data)
            database.write(data)
            database.close()
            return "the book has been saved"
        except:
            database.close()
            return "the book couldn't be saved"
    
    def lookupBook(self):
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