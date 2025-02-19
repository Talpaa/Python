#Exercise 1: Creating an Abstract Class with Abstract Methods
#Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
#Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def perimeter(self)-> float:
        pass
    
    @abstractmethod
    def area(self)-> float:
        pass
    

class Circle(Shape):
    
    def __init__(self, 
                 ray: float) -> None:
        
        self.ray: float = float(ray)

    #2πR
    def perimeter(self)->float:
        
        perimeter: float = (2 * pi * self.ray)

        return round(perimeter, 2)

    #πR**2
    def area(self)->float:

        area: float = (pi * (self.ray ** 2))
        
        return round(area, 2)
    

class Rectangle(Shape):
    
    def __init__(self, 
                 length: float, 
                 width: float) -> None:
        
        self.length: float = float(length)
        self.width: float = float(width)

    def perimeter(self) -> float:
        
        perimeter: float = (2 * self.length)+(2 * self.width)

        return round(perimeter, 2)
    
    def area(self) -> float:
        
        area: float = (self.length * self.width)

        return round(area, 2)

print()
print()    
print()

cerchio: Circle = Circle(ray=1)

print(f'Cerchio:')
print(f'Circonferenza: {cerchio.perimeter()}')
print(f'Area: {cerchio.area()}\n')


rettangolo: Rectangle = Rectangle(length=1, width=2)

print(f'Rettangolo:')
print(f'Perimetro: {rettangolo.perimeter()}')
print(f'Area: {rettangolo.area()}')