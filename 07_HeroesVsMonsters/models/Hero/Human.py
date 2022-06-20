from models.Hero.Hero import Hero

class Human(Hero):
    @property
    def stamina(self):
        return super().stamina + 1

    @property
    def strength(self):
        return super().strength + 1