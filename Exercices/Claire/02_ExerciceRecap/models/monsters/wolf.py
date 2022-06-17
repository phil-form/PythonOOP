from models.monsters.monster import Monster

class Wolf(Monster):

    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        
    def loot(self):
        return {"leather": super().leather}

    def shortName(self) -> str:
        return "W"
        
    def __str__(self):
        return f"[Wolf]: {super().__str__()}"
