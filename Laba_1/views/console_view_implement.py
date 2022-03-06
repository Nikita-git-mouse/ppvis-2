import sys

from interfaces.view_interface import View

class ConsoleView(View):
    def __init__(self):
        pass

    def view(self, location, predators = 0, herbivores = 0):
        sizeX = location.getSizeX()
        sizeY = location.getSizeY()
        for i in range(0, sizeX):
            for j in range(0, sizeY):
                v = False
                for pred in predators:
                    predX = pred.getX()
                    predY = pred.getY()
                    if ( i == predX and j ==predY ):
                        sys.stdout.write('#')
                        v = True
                        break
                if v == True:
                    continue
                for herb in herbivores:
                    herbX = herb.getX()
                    herbY = herb.getY()
                    if ( i == herbX and j ==herbY ):
                        sys.stdout.write('*')
                        v = True
                        break
                if v == True:
                    continue
                if location.getField(i,j) != None:
                    sys.stdout.write('.')
                else:
                    sys.stdout.write(' ')
            sys.stdout.write('\n')

