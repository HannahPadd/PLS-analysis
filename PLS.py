from Book import Book
from User import User
from Commands import Commands
from database import Database
import json

programEnd = 0

#the main loop for the program to run in.
while(programEnd == 0):
    bookDatabase = open("bookDatabase.json", "w+")
    userDatabase = open("userDatabase.json", "w+")

    Commands.userInput = input("type your command:> ")
    
    


    