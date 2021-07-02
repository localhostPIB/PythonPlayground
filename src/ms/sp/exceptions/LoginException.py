class CustomError(Exception):

    def __init__(self, message="Login war nicht erfolgreich !"):
        self.message = message
        super().__init__(self.message)
