

class Customer:
    id=1
    def __init__(self,name, address,email):

        self.id=Customer.id
        Customer.id += 1

        # autoincremented
        self.name=name
        self.address=address
        self.email=email

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    def simple_instance_method(self):
        return self.name

    @staticmethod
    def get_next_id():
        return Customer.id






