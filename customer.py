import json
class user:
    def __init__ (self, userName, userID, userFirstName, userLastName):
        self.userName = userName
        self.userID = userID
        self.userFirstName = userFirstName
        self.userLastName = userLastName

    def CreateUser(self):
        
        saveCustomer = {
            "userName" : self.userName,
            "userLastName" : self.userLastName,
            "userFirstName" : self.userFirstName,
            "userID" : self.userID
        }
        #json.dump(CreateUser)