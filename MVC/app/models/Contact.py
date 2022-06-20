class Contact:
    def __init__(self, email, text) -> None:
        self.email = email
        self.text = text

    def __str__(self) -> str:
        return f"{self.email} {self.text}"

