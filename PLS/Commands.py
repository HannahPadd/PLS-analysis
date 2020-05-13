from User import User
from book import Book



class Commands:
    a = 10
    

    def AddBook(self):
        bookInput = input("""

        give the name of the book:

        """)
        bookAuthor = input("""
        give the name of the writer of the book
        
        """)
        book1 = Book(bookAuthor, bookInput)
        print(book1)


    