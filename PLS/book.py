import json

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.available = True

    def SaveBook(self):
        
        saveBook = {
            "BookAuthor" : self.author,
            "bookTitle" : self.title,
            "bookAvailable" : self.available
        }
        
        saveBook = json.dumps(saveBook) 
        database = open("bookDatabase.json", "r+")
    #try:
        data = json.loads(database)
        data.update(saveBook)
        data = json.dumps(data)
        database.write(data)
        database.close()
        return "the book has been saved"
    #except:
        database.close()
        return "the book couldn't be saved"
    
    
