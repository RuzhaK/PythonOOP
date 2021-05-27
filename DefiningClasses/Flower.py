from dataclasses import  dataclass


@dataclass
class Flower():
    name:str
    water_requirements:int
    is_happy:bool=False

    def water(self,quantity):
        if quantity>=self.water_requirements:
            self.is_happy=True

    def status(self):
        if self.is_happy==True:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
