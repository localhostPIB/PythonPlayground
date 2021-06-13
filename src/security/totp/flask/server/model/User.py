import persistent


class User(persistent.Persistent):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password

    def setUserName(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password
