
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = [[None for _ in range(0, y)] for _ in range (0, x)]

    def getField(self, x, y):
        return self.area[x][y]

    def setField(self, plant):
        x = plant.getX()
        y = plant.getY()
        self.area[x][y] = plant

    def getSizeX(self):
        return self.x

    def getSizeY(self):
        return self.y
        
