from models.Hero.Hero import Hero

class Dwarf(Hero):
    @property
    def stamina(self):
        return super().stamina + 2