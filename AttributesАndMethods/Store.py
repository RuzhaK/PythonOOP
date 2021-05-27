from collections import defaultdict
class Store:
    def __init__(self, name, type, capacity):
        self.items=defaultdict(int)
        self.name=name
        self.type=type
        self.capacity=capacity
    @classmethod
    def from_size (cls,name:str, type:str, size:int):
        capacity=size//2
        return cls(name, type, capacity)

    def add_item(self,item_name:str) :
        products_count=sum(self.items.values())
        if self.capacity>products_count:
            self.items[item_name]+=1
            return f"{item_name} added to the store"

        return f"Not enough capacity in the store"

    def remove_item(self,item_name:str, amount:int) :
        if item_name not in self.items or self.items[item_name]<amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -=amount
        return f"{amount} {item_name} removed from the store"
    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
