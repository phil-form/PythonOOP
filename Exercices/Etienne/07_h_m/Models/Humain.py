from Models.Heros import Heros

class Humain(Heros):
    def __init__(self):
        super().__init__(11, 1, 1)  ## bonus: endurance à 1, force à 1
