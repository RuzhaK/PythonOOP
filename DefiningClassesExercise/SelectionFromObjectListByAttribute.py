class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f'{self.name};{self.age}'

people=[
    Person('Pesho',11),
    Person('Pesho',10),
    Person('Gosho',11)
]



def get_object_by_attr_value(objects, **kwargs):
    result=[]
    for obj in objects:
        is_valid=True
        for key, value in kwargs.items():
            if not hasattr(obj,key)and getattr(obj,key)!=value:
                is_valid=False
                break
        if is_valid==True:
            result.append(obj)

    return result


print(get_object_by_attr_value(people,name='Gosho',age=11))