import json
class user:
    def __init__ (self, userName, userID, userFirstName, userLastName, booksBorrowed):
        self.userName = userName
        self.userID = userID
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.booksBorrowed = booksBorrowed

    def CreateUser():
        
        saveUser = {
            "userName" : self.userName,
            "userLastName" : self.userLastName,
            "userFirstName" : self.userFirstName,
            "userID" : self.userID,
            "booksBorrowed" : self.booksBorrowed
        }
        json.dump(CreateUser)

    def userList():
        pass

with open('users.txt', 'w') as outfile:
    json.dump(CreateUser, outfile)