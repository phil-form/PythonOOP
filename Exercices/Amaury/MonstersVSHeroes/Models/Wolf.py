from Monster import Monster

class Wolf(Monster):

    def __init__(self):
        super().__init__()
        super().initiateRessources('leather')
