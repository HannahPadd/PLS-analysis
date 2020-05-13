import json
import datetime
from User import User
from book import Book


class Database:
    def __init__(self, book, bookId, available, userLend, database):
        self.book = book
        self.bookId = bookId
        self.available = available
        self.userLend = userLend
        self.bookDatabase = open("bookDatabase.json", "w+")
    

    def save(self):
        toSave = {
            "bookId" : self.bookId,
            "book" : self.book,
            "available" : self.available,   
            "userLend" : self.userLend
        }
        json.dump(toSave, self.bookDatabase)

    def load(self):
        pass

    



