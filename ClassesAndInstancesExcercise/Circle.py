class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def set_radius(self,new_radius):
        self.radius=new_radius
    def get_area(self):
        return round(Circle.pi*(self.radius*self.radius),2)
    def get_circumference(self):
        return f"{2*Circle.pi*self.radius}"



circle = Circle(11)
print(circle.get_area())
print(circle.get_circumference())
# todo  80 / 100