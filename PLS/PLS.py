from book import Book
from User import User
from Commands import Commands
import json

programEnd = 0
bookDatabase = open("bookDatabase.json", "w+")
userDatabase = open("userDatabase.json", "w+")

#the main loop for the program to run in.
while(programEnd == 0):
    userInput = input("""
Press 1 to create an customer:
Press 2 to create a book:
Press 3 to Lend a book out:
Press 4 to return a book: 
Press 5 to Search for a book:
""")
    if userInput == "1":
        print ("1")
    if userInput == "2":
        Commands.AddBook(0)
    if userInput == "3":
        print("3")
    if userInput == "4":
        print("4")
    if userInput == "5":
        print("5")
    
    


    