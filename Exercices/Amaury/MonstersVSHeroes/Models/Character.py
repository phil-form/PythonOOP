from Dice import Dice

class Character():

    def __init__(self):
        self.__force = self.__createForceOrEndurance()
        self.__endurance = self.__createForceOrEndurance()
        self.__hp = self.__createHp()

    @property
    def force(self):
        return self.__force

    @property
    def endurance(self):
        return self.__endurance

    @property
    def hp(self):
        return self.__hp

    def __createForceOrEndurance(self):
        temp = []
        res = []
        sum = 0

        for i in range(4):
            dice = Dice(6)
            temp.append(dice.roll())
        
        for i in range(3):
            res.append(max(temp))

        for i in range(len(res)):
            sum += res[i]

        return sum

    def __createHp(self):
        base = self.__endurance
        modifier = self.__modifier(self.__endurance)

        
    def __modifier(self, prop):
        if prop < 5:
            return -1
        elif prop < 10:
            return 0
        elif prop < 15:
            return 1
        else:
            return 2


    def hit(self):
        dice = Dice(4)
        modifier = self.__modifier(self.__force)
        return dice.roll() + modifier