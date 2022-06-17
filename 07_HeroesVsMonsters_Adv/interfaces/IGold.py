from abc import ABC, abstractmethod

class IGold(ABC):
    @abstractmethod
    def getGold(self):
        pass