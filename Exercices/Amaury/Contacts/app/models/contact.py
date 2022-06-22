class Contact:
    def __init__(self, id, firstname: str, lastname: str, email: str, password: str) -> None:
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password