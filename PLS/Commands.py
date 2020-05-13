from User import User
from book import Book



class Commands:

    def AddBook(self):
        bookInput = input("what's the name of the book:> ")
        bookAuthor = input("Who is the author:> ")
        book = Book(bookInput, bookAuthor)
        print(book.CreateBook())




    