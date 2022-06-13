from Models.Address import Address

class Home:
    def __init__(self, address: Address, surface: int, nbRooms: int, nbFloors: int, gardenSqMtr: int = 0) -> None:
        self.__address = address
        self.__surface = surface
        self.__nbRooms = nbRooms
        self.__nbFloors = nbFloors
        self.__gardenSqMtr = gardenSqMtr

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value