Лабораторная работа №1
===========

### **Тема**: Модель животного мира<br>

### **Предметная область**: взаимодействие жителей леса в формате игровой симуляции<br>
### **Важные сущности**:<br>
**Элемент симуляции** - интерфейс, который будет имплементирован в каждой сущности нашей симуляции.<br>

```mermaid
classDiagram
  direction LR
  class ElementSimulation {
  <<interface>>
    + step()
  }
```
  
<h4>Живой организм<br>

```mermaid
classDiagram
  direction LR
  class Organism {
  <<interface>>
    - health: number
    - ageLife: number
    + Organism(health, age)
    + reproduction()
  }
```
  
Растения<br>
```mermaid
classDiagram
  direction LR
  
  class Organism {
  <<interface>>
    - health: number
    - ageLife: number
    + Organism(health, age)
    + reproduction()
  }
  
  class ElementSimulation {
  <<interface>>
    + step()
  }
  
  class Plant {
    - health: number
    - ageLife: number
    + Plant()
    + step()
    + reproduction()
  }
  
    
   Plant --|> Organism
   Plant ..|> ElementSimulation
 ```

 <h4>Локация<br>

```mermaid
classDiagram
  direction LR
  class ElementSimulation {
  <<interface>>
    + step()
  }

  class Plant {
    - health: number
    - ageLife: number
    + Plant()
    + step()
    + reproduction()
  }
   
  class Location {
    -area : Plant[][]
    -growthFreq: number
    + Location(sizeX, sizeY)
    + setGrowthFreq(number)
    + step()
    + getField(x, y)
    + clearField(x, y)
  }

 Location ..|> ElementSimulation
 Location *-- Plant
```
  
  
<h4>Животное<br>
  
```mermaid
classDiagram
  direction LR
    class Organism {
  <<interface>>
    - health: number
    - ageLife: number
    + Organism(health, age)
    + reproduction(): Organism
  }
  
  class ElementSimulation {
  <<interface>>
    + step()
  }
  
  class Animal {
    <<interface>>
    - position X: number
    - position Y: number
    - health: number
    - ageLife: number
    - area: Location
    + Animal(positionX, positionY, area, health, ageLife)
    + reproduction()
    + eat()
    + step()
  }
  
   Animal --|> Organism
   Animal ..|> ElementSimulation
``` 
  


<h4>Хищник<br>
  
```mermaid
classDiagram
  direction LR
  class Predator {
    - position X: number
    - position Y: number
    - health: number
    - ageLife: number
    - area: Location
    + Predator(positionX, positionY, area, health, ageLife)
    + reproduction()
    + eat()
    + step()
  }
  
  class Animal {
    - position X: number
    - position Y: number
    - health: number
    - ageLife: number
    - area: Location
    + Animal(positionX, positionY, area, health, ageLife)
    + reproduction()
    + eat()
    + step()
  }

   Predator ..|> Animal
``` 
 
 <h4>Травоядные<br>
  
```mermaid
classDiagram
  direction LR
  class Predator {
    - position X: number
    - position Y: number
    - health: number
    - ageLife: number
    - area: Location
    + Predator(positionX, positionY, area, health, ageLife)
    + reproduction()
    + eat()
    + step()
  }
  
  class Herbivore {
    - position X: number
    - position Y: number
    - health: number
    - ageLife: number
    - area: Location
    + Animal(positionX, positionY, area, health, ageLife)
    + reproduction()
    + eat()
    + step()
  }

   Herbivore ..|> Animal
``` 
### **Вывод в консоль:**
   
 \# - хищник<br>
 \* - травоядный<br>
 \. - растительность<br>
   
**Локация в консоле:**<br>

   ![Alt-текст](https://avatars1.githubusercontent.com/u/5384215?v=3&s=460 "Орк")
