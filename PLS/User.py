import json
import csv


class User():
    def __init__(self, Gender, NameSet, GivenName, Surname, StreetAdress, ZipCode, City, EmailAdress, Username, TelephoneNumber):
        self.gender = Gender
        self.nameSet = NameSet
        self.givenName = GivenName
        self.Surname = Surname
        self.streetAdress = StreetAdress
        self.zipCode = ZipCode
        self.city = City
        self.emailAdress = EmailAdress
        self.userName = Username
        self.telephoneNumber = TelephoneNumber

    def listUsers(self):
        users = open("FakeNameSet20.csv", "r")
        print(users)


    def SaveUser(self):
        with open('FakeNameSet20.csv', mode = 'w', newline = '') as users:
            addingUser = csv.writer(users)
        Gender = input("Whats is your gender")
        NameSet = input("Whats is your nameSet")
        GivenName = input("Whats is your givenName")
        Surname = input("Whats is your Surname")
        StreetAdress = input("Whats is your streetAdress")
        ZipCode = input("Whats is your zipCode")
        City = input("Where do you life")
        EmailAdress = input("Whats is your emailAdress")
        Username = input("Whats is your userName")
        TelephoneNumber = input("Whats is your telephoneNumber")

        users.writerow([Gender, NameSet, GivenName, Surname, StreetAdress, ZipCode, City, EmailAdress, Username, TelephoneNumber])

User.SaveUser
"""
    def SaveUser(self):
        
        saveUser = {
            "userName" : self.userName,
            "userLastName" : self.userLastName,
            "userFirstName" : self.userFirstName,
        }
        
        saveUser = json.dumps(saveUser)
        database = open("database.json", "w")
        try:
            database.write(saveUser)
            database.close()
            print("the user has been saved")
        except:
            database.close()
            print("the user couldn't be saved")
"""
   