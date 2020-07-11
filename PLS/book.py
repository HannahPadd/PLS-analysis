import json

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
    
    def LookupBook(self):
        with open("booksset1.json", 'r') as bookDatabase:
            bookDatabase = json.load(bookDatabase)
        searchType = input("""do you want to search via:
        - title
        - author
        - ISBN
        Type the word for the search key
        """)
        searchType.lower()
        searchCount = 0
        if (searchType == "title"):
            searchKey = input("Enter the title:> ")
            for i in bookDatabase:
                if (bookDatabase[searchCount]["title"] == searchKey):
                    print("this book is at our library")
                    return
                else:
                    searchCount += 1
            print("We don't have this book in our library")

        if (searchType == "author"):
            searchKey = input("Enter the author:> ")
            for i in bookDatabase:
                if (bookDatabase[searchCount]["author"] == searchKey):
                    print("I don't know what to do here")
                else:
                    searchCount += 1

        if (searchType == "isbn"):
            searchKey = input("Enter the ISBN:> ")
            for i in bookDatabase:
                if (bookDatabase[searchCount]["isbn"] == searchKey):
                    print("This book is in our library")
                else:
                    searchCount += 1
            print("We do not have this book in our library")