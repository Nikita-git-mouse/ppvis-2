from location.location_implement import Location
from views.console_view_implement import ConsoleView
from plant.plant_implement import Plant
from animal.herbivore_implement import Herbivore
from animal.predator_implement import Predator

from random import randint


area = Location(50, 50)

area.setField(Plant(2,3))
area.setField(Plant(5,7))
area.setField(Plant(2,25))
area.setField(Plant(4,23))
area.setField(Plant(23,12))
area.setField(Plant(45,32))
area.setField(Plant(43,45))

herbivores = [Herbivore(randint(0, 50), randint(0, 50)) for _ in range(0, 15)]
predators = [Predator(randint(0, 50), randint(0, 50)) for _ in range(0, 15)]

viewer = ConsoleView()

viewer.view(area, predators, herbivores)



