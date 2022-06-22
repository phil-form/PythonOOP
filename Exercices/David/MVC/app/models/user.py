class user:
    def __init__(self, userid, username, password, mail, description= None):
        self.userid      = userid
        self.username    = username
        self.password    = password
        self.mail        = mail
        self.description = description