from Model import Model

class Login(Model):

    def __init__(self):
        super().__init__("login",["username","password"])

    