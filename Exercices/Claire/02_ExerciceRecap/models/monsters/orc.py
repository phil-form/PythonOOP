from models.monsters.monster import Monster

class Orc(Monster):

    def __init__(self, posX, posY):
        super().__init__(posX, posY, hasGold=True)

    @property
    def strength(self) -> int:
        return super().strength + 1

    def loot(self):
        return {"gold": self.gold}

    def shortName(self) -> str:
        return "O"
        
    def __str__(self):
        return f"[Orc] {super().__str__()}"
