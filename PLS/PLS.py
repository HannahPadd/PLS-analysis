from book import Book
from customer import Customer
from Commands import Commands
import json

programEnd = 0

#the main loop for the program to run in.
while(programEnd == 0):
    userInput = Command(input("Type your command:> "))
    
    