import json
import shutil
import os
# class Backup:
#    def createBackup(self):
#        try:
#            booksData = open("books.json", "r")
#            customerData = open("customer.json", "r")
#        except:
#            print("one or more databses are missing!\nbackup could not be created.")
#            return
#        shutil.copy(booksData, "booksold.json")
#        shutil.copy(customerData, "customerold.json")
#        print("backup created successfully.")
#
#
#    def restoreBackup(self):
#        try:
#            os.rename("booksold.json", "books.json")
#            os.rename("customerold.json", "customer.json")
#        except:
#            print("The backup could not be restored.")
#            return
#        print("The backup was succesfully restored")
        
def BackUp():
    os.chdir("C:\\Users\eigenaar\Documents\school\PLS-analysis\PLS\\")
    shutil.copy("userDatabase.json", "C:\\Users\eigenaar\Documents\school\PLS-analysis\PLS\Back_up\\")
    shutil.copy("booksset.json", "C:\\Users\eigenaar\Documents\school\PLS-analysis\PLS\Back_up\\")
    shutil.copy("FakeNameSet20.csv", "C:\\Users\eigenaar\Documents\school\PLS-analysis\PLS\Back_up\\")
    shutil.copy("bookDatabase.json", "C:\\Users\eigenaar\Documents\school\PLS-analysis\PLS\Back_up\\")