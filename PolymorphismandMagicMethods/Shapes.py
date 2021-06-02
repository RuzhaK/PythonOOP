import math
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.__r=r
    def calculate_area(self):
        return self.__r*self.__r*math.pi
    def calculate_perimeter(self):
        return 2*math.pi*self.__r

class Rectangle(Shape):
    def __init__(self,height, weight):
        self.__height=height
        self.__weight=weight
    def calculate_area(self):
        return self.__height*self.__weight
    def calculate_perimeter(self):
        return self.__height*2+2*self.__weight

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
