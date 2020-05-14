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

    def listUsers():
        users = open("FakeNameSet20.csv", "r")
        print(users)


    def SaveUser():
        with open('FakeNameSet20.csv', mode = 'w', newline = '') as users:
            addingUser = csv.writer(users)
        gender = input("Whats is your gender")
        nameSet = input("Whats is your nameSet")
        givenName = input("Whats is your givenName")
        Surname = input("Whats is your Surname")
        streetAdress = input("Whats is your streetAdress")
        zipCode = input("Whats is your zipCode")
        city = input("Where do you life")
        emailAdress = input("Whats is your emailAdress")
        userName = input("Whats is your userName")
        telephoneNumber = input("Whats is your telephoneNumber")

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
   