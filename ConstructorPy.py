class chrome:

    def __init__(self,URL, uname, pwd):
        self.website = URL
        self.username = uname
        self.password = pwd
        if self.username == "":
            self.username = "admin"
        if (self.username == "admin") and (self.password == ""):
            self.password = "Password"
        else:
            print("Enter a password")

    def loadAddress(self):
        print("Loading the URL," + self.website + " in Chrome", "username : ", self.username, " and password : ",self.password)

    def refresh(self):
        print("Refreshing the URL," + self.website + " in Chrome", "username : ", self.username, " and password : ",self.password)

class firefox():

    def loadAddress(self,URL):
        print("Loading the URL," + URL + " in firefox")

obj = chrome("www.google.co.in","","")
obj.loadAddress()
obj.refresh()
