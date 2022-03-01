from interfaces.organism_interface import Organism

class Herbivore(Organism):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
