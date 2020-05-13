import json

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.available = True

    def CreateBook(self):
        
        saveBook = {
            "BookAuthor" : self.author,
            "bookTitle" : self.title,
            "bookAvailable" : self.available
        }
        
        saveBook = json.dumps(saveBook) 
        database = open("bookDatabase.json", "w")
        try:
            database.update(saveBook)
            database.close()
            print("the book has been saved")
        except:
            database.close()
            print("the book couldn't be saved")
    
    
