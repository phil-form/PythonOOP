from Character import Character

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.__stock = {'gold': 0, 'leather': 0}
        self.x = 0
        self.y = 0

    @property
    def stock(self):
        return self.__stock

    def strip(self, enemy):
        self.__stock['gold'] += enemy.gold
        self.__stock['leather'] += enemy.leather

    def move(self):
        direction = input('Enter the direction to go ?: ')
        if direction == 'up':
            self.y += 1
        if direction == 'down':
            self.y -= 1
        if direction == 'right':
            self.x += 1
        if direction == 'left':
            self.x -= 1

    