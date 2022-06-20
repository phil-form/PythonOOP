from toolBox.Dice import Dice

class Generator:
    @staticmethod
    def getStat(nbThrow = 4):
        dice = Dice(6)
        stats = []

        for i in range(nbThrow):
            stats.append(dice.throw())

        if __name__ == '__main__':
            print(stats)

        stats.sort()
        stats.remove(stats[0])

        if __name__ == '__main__':
            print(stats)

        return sum(stats)

    def getModif(value):
        if(value < 5):
            return -1
        elif (value < 10):
            return 0
        elif (value < 15):
            return 1
        else:
            return 2