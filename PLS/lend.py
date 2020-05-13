import book 
import json

class Lend():
    def Lend():
        if bookAvailable == True:
            bookAvailable = False
            print("You are now borrowing this book")
        else: 
            print("Book is not avaliable")
    def Return():
        if bookAvailable == False:
            bookAvailable = True
            print("You have now raturned this book")
        else:
            print("this book was never borrowed")