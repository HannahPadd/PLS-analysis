from Commands import Commands
import json
import Backup
from book import Book

programEnd = 0
bookDatabase = open("bookDatabase.json", "w+")
userDatabase = open("userDatabase.json", "w+")

#the main loop for the program to run in.
while(programEnd == 0):
    userInput = input("""
Press 1 to create an customer:
Press 2 to create a book:
Press 3 to return a book out:
Press 4 to lend a book: 
Press 5 to Search for a book:
Press 6 to Back up:
Press 7 to retrieve back up:
Write done to close program:
""")
    if userInput == "1":
        Commands.AddUser(0)
    if userInput == "2":
        Commands.AddBook(0)
    if userInput == "3":
        Commands.BookReturn(0)
    if userInput == "4":
        Commands.BookLend(0)
    if userInput == "5":
        Commands.SearchBook(0)
    if userInput == "6":
        Backup.BackUp()
    if userInput == "7":
        Backup.retrieve_BackUp()
    if userInput == "8":
        Book.ImportFromDB(0)
    if userInput == "done":
        Backup.BackUp()
        break
        
        
