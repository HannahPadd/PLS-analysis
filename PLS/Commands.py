from User import User
import Book
import Lend
import Search


class Commands:

    def AddBook(self):
        bookInput = input("what's the name of the book:> ")
        bookAuthor = input("Who is the author:> ")

        book = Book(bookInput, bookAuthor)
        Book.SaveBook(book)

    def AddUser(self):
        Gender = input("Whats is your gender:> ")
        NameSet = input("Whats is your nameSet:> ")
        GivenName = input("Whats is your givenName:> ")
        Surname = input("Whats is your Surname:> ")
        StreetAdress = input("Whats is your streetAdress:> ")
        ZipCode = input("Whats is your zipCode:> ")
        City = input("Where do you life:> ")
        EmailAdress = input("Whats is your emailAdress:>")
        Username = input("Whats is your userName:> ")
        TelephoneNumber = input("Whats is your telephoneNumber:> ")

        user = User(Gender, NameSet, GivenName, Surname, StreetAdress, ZipCode, City, EmailAdress, Username, TelephoneNumber)
        User.SaveUser(user)

    def BookReturn(self):
        Lend.BookReturn(0)
        
    def BookLend(self):
        Lend.BookLend(0)
        
    def SearchBook(self):
        Search.Search(0)
        


