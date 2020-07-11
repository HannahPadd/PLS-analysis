import json
import csv


class User:
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
        with open('FakeNameSet20.csv', 'a+', newline='') as FakeName_file:
            saveUsers = csv.writer(FakeName_file)
            saveUsers.writerow([self.gender, self.nameSet, self.givenName, self.Surname, self.streetAdress, self.zipCode, self.city, self.emailAdress, self.userName, self.telephoneNumber])


#User.SaveUser(i,i,i,i,i,i,i,i,i,i)
