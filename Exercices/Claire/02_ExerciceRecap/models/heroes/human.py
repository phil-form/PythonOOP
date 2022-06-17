from models.heroes.hero import Hero

class Human(Hero):

    def __init__(self, name, posX, posY):
        super().__init__(name, posX, posY)

    @property
    def stamina(self) -> int:
        return super().stamina + 1

    @property
    def strength(self) -> int:
        return super().strength + 1

    def __str__(self):
        return f"[Human]{self.name}: {self.currentHp}/{self.hp}"