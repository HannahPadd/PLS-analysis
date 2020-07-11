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
location = "/PLS-analysis/PLS"
def BackUp():
    location = os.path.dirname(os.path.realpath(__file__)) 
    os.chdir(location)
    shutil.copy("userDatabase.json",location + "\Back_up")
    shutil.copy("bookDatabase.json", location + "\Back_up")
    shutil.copy("FakeNameSet20.csv", location + "\Back_up")
    shutil.copy("bookDatabase.json", location + "\Back_up")