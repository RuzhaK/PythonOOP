from .dvd import DVD
class Customer:
    def __init__(self, name,age,id):
        self.rented_dvds=[]
        self.name=name
        self.id=id
        self.age=age


    def __repr__(self):
        dvd_names=', '.join([dvd.name for dvd in self.rented_dvds])
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({dvd_names})"

    def has_dvd(self,dvd:DVD):
        return dvd in self.rented_dvds

    def add_dvd(self,dvd:DVD):
        self.rented_dvds.append(dvd)

    def remove_dvd(self,dvd:DVD):
        if dvd in self.rented_dvds:
            self.rented_dvds.remove(dvd)