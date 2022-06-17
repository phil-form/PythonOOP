from abc import ABC
from models.Character import Character

class Monster(Character, ABC):
    def __init__(self, coord) -> None:
        super().__init__(coord)
        self.__hidden = True

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, value: bool):
        self.__hidden = value