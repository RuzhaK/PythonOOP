from .dvd import DVD
from .customer import Customer

class MovieWorld:
    _DVD_CAPACITY=15
    _CUSTOMER_CAPACITY=10
    def __init__(self,name):
        self.name=name
        self.customers=[]
        self.dvds=[]
        self.dvd_ids={}
        self.customer_ids= {}
    @classmethod
    def dvd_capacity(cls):
        return cls._DVD_CAPACITY
    @classmethod
    def customer_capacity(cls):
        return cls._CUSTOMER_CAPACITY
    def add_customer(self,customer: Customer) :
        if len(self.customers)<self._CUSTOMER_CAPACITY:
            self.customers.append(customer)
            self.customer_ids[customer.id]=customer

    def add_dvd(self,dvd: DVD) :
        if len(self.dvds) < self._DVD_CAPACITY:
            self.dvds.append(dvd)
            self.dvd_ids[dvd.id]=dvd

    def rent_dvd(self,customer_id: int, dvd_id: int):
        dvd=self.dvd_ids.get(dvd_id)
        customer=self.customer_ids.get(customer_id)
        if customer.has_dvd(dvd):
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age<dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.add_dvd(dvd)
        dvd.rent()
        return f"{customer.name} has successfully rented {dvd.name}"
    def return_dvd(self,customer_id, dvd_id) :
        dvd = self.dvd_ids.get(dvd_id)
        customer = self.customer_ids.get(customer_id)
        if not customer.has_dvd(dvd):
            return f"{customer.name} does not have that DVD"
        customer.remove_dvd(dvd)
        dvd.unrent()

        return f"{customer.name} has successfully returned {dvd.name}"
    def __repr__(self) :
        customers=list(map(str,self.customers))
        dvds=list(map(str,self.dvds))
        return '\n'.join(customers+dvds)

