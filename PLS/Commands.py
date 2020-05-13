from User import User
from book import Book



class Commands:
    a = 10
    

    def AddBook(self):
        bookInput = input("""

give the name of the book:

""")
        bookAuthor = input("""
give the name of the writer of the book:

""")
        book = Book(bookAuthor, bookInput)
        Book.SaveBook(book)

    def AddUser(self):
        username = input("""
Please enter your username:
""")
        firstname = input(""" 
Please enter your first name:
""")
        lastname = input("""
Please enter your last name:
""")
        user = User(username, firstname, lastname)
        User.SaveUser(user)

    