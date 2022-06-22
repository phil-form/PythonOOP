

class User:
    def __init__(self, userid, username, userpassword, email, userdescription):
        self.__userid = userid
        self.__username = username
        self.__userpassword = userpassword
        self.__email = email
        self.__userdescription = userdescription

    @property
    def userid(self):
        return self.__userid

    @userid.setter
    def userid(self, value):
        self.__userid = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        self.__username = value

    @property
    def userpassword(self):
        return self.__userpassword

    @userpassword.setter
    def userpassword(self, value: str):
        self.__userpassword = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value

    @property
    def userdescription(self):
        return self.__userdescription

    @userdescription.setter
    def userdescription(self, value: str):
        self.userdescription = value

    def __str__(self):
        return f"{self.username} [{self.email}]"
