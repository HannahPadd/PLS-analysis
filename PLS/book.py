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
        

    def ImportFromDB(self):
        with open("booksset.json", 'r+', encoding='utf-8') as importBookDatabase:
            importBookDatabase = json.load(importBookDatabase)
        bookDatabase = open("bookDatabase.json", 'a+', encoding='utf=8')
        json.dump(importBookDatabase, bookDatabase)
        bookDatabase.close()

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
            if done == False:
                print("book not found")
    
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
                
    def SaveBook(self, ISBN):
        #saveBook = json.dumps(self.__dict__)
        """
        with open('Books.csv', 'a+', newline='') as books:
            saveBooks = csv.writer(books)
            saveBooks.writerow([self.title.lower(), ISBN, None])
            """
        with open("bookDatabase.json", 'a+', newline='') as bookDatabase:
            bookDatabase = json.load(bookDatabase)
            entry = {}


        
    
    def LookupBook(self):
        with open("bookDatabase.json", 'r', encoding='utf-8') as bookDatabase:
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
            bookList = []
            for i in bookDatabase:
                if (searchCount == len(bookDatabase)):
                    break
                elif (bookDatabase[searchCount]["author"] == searchKey):
                    bookList.append(str(bookDatabase[searchCount]["title"]))
                    searchCount += 1
                else:
                    searchCount += 1

            if (len(bookList) > 0):
                print("There are books from this author in our library:\n".join(bookList))
            else:
                print("There aren't any books by this author in our library")

        if (searchType == "isbn"):
            searchKey = input("Enter the ISBN:> ")
            for i in bookDatabase:
                if (bookDatabase[searchCount]["isbn"] == searchKey):
                    print("This book is in our library")
                else:
                    searchCount += 1
            print("We do not have this book in our library")