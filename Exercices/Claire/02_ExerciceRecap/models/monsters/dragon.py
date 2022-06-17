from models.monsters.monster import Monster

class Dragon(Monster):

    def __init__(self, posX, posY):
        super().__init__(posX, posY, True, True)

    @property
    def stamina(self) -> int:
        return super().stamina + 1

    def loot(self):
        return {"gold": super().gold, "leather": super().leather}

    def shortName(self) -> str:
        return "D"
        
    def __str__(self):
        return f"[Dragon]: {super().__str__()}"
