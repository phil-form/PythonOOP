from abc import ABC, abstractmethod

class ILeather(ABC):
    @abstractmethod
    def getLeather(self):
        pass