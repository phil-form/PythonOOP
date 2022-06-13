class Address:
    def __init__(self, street, number, town, zipCode) -> None:
        self.street = street
        self.number = number
        self.town = town
        self.zipCode = zipCode

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value: str):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: int):
        self.__number = value

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, value: str):
        self.__town = value

    @property
    def zipCode(self):
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, value: int):
        if value > 999 and value < 10000:
            self.__zipCode = value
        else:
            print("Zip code must be 999 > and < 10000")