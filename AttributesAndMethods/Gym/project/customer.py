def generic_init(self,*args):
    attributes=self.__annotations__
    for attr, value in zip(attributes,args):
        if attr=='_id':
            continue
        setattr(self,attr,value)
    self.id=self.__class__._id
    self.__class__._id += 1

class Customer:
    name:str
    address:str
    email:str
    _id=1

    __init__=generic_init
    # def __init__(self,name, address,email):
    #     self.id=self._id
    #     self.__class__._id+=1
    #
    #
    #     # autoincremented
    #     self.name=name
    #     self.address=address
    #     self.email=email

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @classmethod
    def get_next_id(cls):
        return cls._id


