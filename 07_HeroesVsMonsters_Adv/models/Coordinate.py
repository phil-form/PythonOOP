class Coordinate:
    def __init__(self, posX, posY) -> None:
        self.__x = posX
        self.__y = posY

    @property
    def posX(self):
        return self.__x

    @posX.setter
    def posX(self, value):
        self.__x = value

    @property
    def posY(self):
        return self.__y

    @posY.setter
    def posY(self, value):
        self.__y = value

    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o, Coordinate)):
            return self.__x == __o.__x and self.__y == __o.__y
        return False

    def __str__(self) -> str:
        return f"{self.posX} | {self.posY}"