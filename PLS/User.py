import json
class User:
    def __init__ (self, userName, userFirstName, userLastName):
        self.userName = userName
        self.userFirstName = userFirstName
        self.userLastName = userLastName

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
