from User import User
from book import Book
from lend import Lend


class Commands:

    def AddBook(self):
        bookInput = input("what's the name of the book:> ")
        bookAuthor = input("Who is the author:> ")

        book = Book(bookInput, bookAuthor)
        Book.SaveBook(book)

    def AddUser(self):
        username = input("please enter ur username:> ")
        firstname = input("Please enter your first name:> ")
        lastname = input("Please enter your last name:> ")

        user = User(username, firstname, lastname)
        User.SaveUser(user)

    def BookReturn(self):
        bookReturn = input("please enter the book you like to return:> ")
        
        
    def BookLend(self):
        bookLend = input("please enter the book you like to lend:> ")
        Lend(bookLend)

    def searchBook(self):
        searchBook = input("please enter the book you like to search:> ")
        
        
