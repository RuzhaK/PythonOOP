from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height

class Triangle(Shape):

    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calculate_area(self):
        return self.side*self.height/2

class AreaCalculator:

    def __init__(self, shapes):

        
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total
    def add_shape(self,shape):
        self.shapes.append(shape)
        
    @property
    def shapes(self):
        return self.__shapes
    
    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise TypeError("`shapes` should be of type `list`.")
        res=[shape for shape in value if not isinstance(shape,Shape)]
        if res:
            raise TypeError("All elements must be of type Shape")
        self.__shapes=value

shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)