from Models.Heros import Heros

class Nain(Heros):
    def __init__(self):
        super().__init__(12, 0, 2)  ## bonus: endurance à 0, force à 2
