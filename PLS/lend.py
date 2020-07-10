import Book 
import json

class lend:
    def BookLend(self):
        if bookAvailable == True:
            bookAvailable = False
            print("You are now borrowing this book")
        else: 
            print("Book is not avaliable")


    def BookReturn(self):
        if bookAvailable == False:
            bookAvailable = True
            print("You have now raturned this book")
        else:
            print("this book was never borrowed")