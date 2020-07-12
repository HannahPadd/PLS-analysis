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
        

    def ImportFromDB(self):
        with open("booksset.json", 'r+') as importBookDatabase:
            importBookDatabase = json.load(importBookDatabase)
        bookDatabase = open("bookDatabase.json", 'w+')
        json.dump(importBookDatabase, bookDatabase)
        bookDatabase.close()
        
        f = open("Books.csv", "w+")
        f.close()

    def ReturnBook(self, Book, User):
        with open("Books.csv", "rt", newline='') as ReadFile:
            lines = list(csv.reader(ReadFile))

        with open("Books.csv", "wt", newline='') as WriteFile:
            done = False
            Writer = csv.writer(WriteFile)
            for row in lines:
                if row[0] == Book and row[1] == User.lower():
                    if done == False:
                        print(Book + "is being returned by " + User.lower())
                        row[2] = None
                        done = True
                        Writer.writerow(row)
                    else:
                        Writer.writerow(row)
                else:
                    Writer.writerow(row)
            if done == False:
                print("book not found or user not found")
    
    def LendBook(self, Book, User):
        correctUser = False
        with open("FakeNameSet20.csv", "rt", newline='') as Users:
            name = list(csv.reader(Users))
            for row in name:
                if row[2] == User:
                    correctUser = True
            if correctUser == False:
                print("there was no user with the name " + User)
                return
                    

        with open("Books.csv", "rt", newline='') as ReadFile:
            lines = list(csv.reader(ReadFile))

        with open("Books.csv", "wt", newline='') as WriteFile:
            done = False
            Writer = csv.writer(WriteFile)
            for row in lines:
                if row[0] == Book and row[1] == "":
                    if done == False:
                        print(Book + "is being lend to " + User.lower())
                        row[1] = User.lower()
                        done = True
                        Writer.writerow(row)
                    else:
                        Writer.writerow(row)
                else:
                    Writer.writerow(row)
            if done == False:
                print("book not found or user not found")
                
    def SaveBook(self, ISBN):
        searchCount = 0
        with open("bookDatabase.json", 'r', encoding='utf-8') as bookDatabase:
            bookDatabase = json.load(bookDatabase)
        for i in bookDatabase:
            if (bookDatabase[0]["title"] == self.title):
                with open('Books.csv', 'a+', newline='') as books:
                    saveBooks = csv.writer(books)
                    saveBooks.writerow([self.title.lower(), ISBN, None])
                    return
            else:
                searchCount += 1
        
        bookDatabase2 = open("bookDatabase.json" , "r+")
        bookDatabase2 = json.load(bookDatabase2)
        entry = {
            "author" : self.author,
            "country" : self.country,
            "language" : self.language,
            "pages" : self.pages,
            "title" : self.title,
            "year" : self.year
        }
        json.dump(entry, bookDatabase2)

        
        with open('Books.csv', 'a+', newline='') as books:
            saveBooks = csv.writer(books)
            saveBooks.writerow([self.title.lower(), None])
            
        


        
    
    def LookupBook(self):
        with open("bookDatabase.json", 'r', encoding='utf-8') as bookDatabase:
            bookDatabase = json.load(bookDatabase)
        searchType = input("""do you want to search via:
        - title
        - author
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

        