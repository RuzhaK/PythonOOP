import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def set_x(self,new_x):
        self.x=new_x
    def set_y(self,new_y):
        self.y=new_y
    def distance(self,x, y):
        delta_x=abs(x-self.x)
        delta_y=abs(y-self.y)
        return math.sqrt(delta_x**2+delta_y**2)





