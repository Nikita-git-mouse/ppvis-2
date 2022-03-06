import sys

from interfaces.organism_interface import Organism

class Plant(Organism):
    def __init__(self, x, y):
        super().__init__(x, y)
