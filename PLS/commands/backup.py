import json

class databse:
    def __init__(self, book, bookId, available, userLend):
        self.book = book
        self.bookID = bookId
        self.available = available
        self.userLend = userLend

    def jsoncreate():
        database = open("database.json", "w+")

    def save():
        
        toSave = {
            "bookId" : self.bookId,
            "book" : self.book,
            "available" : self.available,   
            "userLend" : self.userLend
        }
        json.dump(toSave, database)

    def load():
