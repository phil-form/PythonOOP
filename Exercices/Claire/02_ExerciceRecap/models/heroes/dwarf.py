from models.heroes.hero import Hero

class Dwarf(Hero):

    def __init__(self, name, posX, posY):
        super().__init__(name, posX, posY)

    def __str__(self):
        return f"[Dwarf]{self.name}: {self.currentHp}/{self.hp}"

    @property
    def stamina(self) -> int:
        return super().stamina + 2