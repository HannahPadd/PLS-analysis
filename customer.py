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
        
        saveCustomer = json.dumps(saveCustomer)
        database = open("database.json", "w")
        try:
            database.write(saveCustomer)
            database.close
            print("the user has been saved")
        except:
            print("the user couldn't be saved")
