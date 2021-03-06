class Zoo:
    def __init__(self,name, budget, animlal_capacity, workers_capacity):
        self.__animal_capacity=animlal_capacity
        self.__workers_capacity=workers_capacity
        self.__budget=budget
        self.name=name
        self.animals=[]
        self.workers=[]


    def add_animal(self,animal, price):
        if len(self.animals)<self.__animal_capacity:
            if price>self.__budget:
                return "Not enough budget"
            self.__budget-=price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return "Not enough space for animal"


    def hire_worker(self,worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"


    def fire_worker(self,worker_name):
        try:
            current_worker=[w for w in self.workers if w.name==worker_name][0]

            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        all_salaries_to_pay=sum([w.salary for w in self.workers])
        if self.__budget>=all_salaries_to_pay:
            self.__budget -= all_salaries_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount_needed=sum([a.get_needs() for a in self.animals])
        if self.__budget>=amount_needed:
            self.__budget -= amount_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."
    def profit(self,amount):
        self.__budget+=amount
    def animals_status(self):
        lions=[a for a in self.animals if a.__class__.__name__=='Lion']
        tigers=[a for a in self.animals if a.__class__.__name__=='Tiger']
        cheetahs=[a for a in self.animals if a.__class__.__name__=='Cheetah']
        result= f"You have {len(self.animals)} animals"+'\n'
        result+=f"----- {len(lions)} Lions:"+'\n'
        result+="{}".format('\n'.join([repr(l) for l in lions]))+'\n'
        result += f"----- {len(tigers)} Tigers:"+'\n'
        result += "{}".format('\n'.join([repr(l) for l in tigers])) + '\n'
        result += f"----- {len(cheetahs)} Cheetahs:"+'\n'
        result += "{}".format('\n'.join([repr(l) for l in cheetahs]))
        return result
    def workers_status(self):
        keepers=[w for w in self.workers if w.__class__.__name__=='Keeper']
        vets=[w for w in self.workers if w.__class__.__name__=='Vet']
        caretakers=[w for w in self.workers if w.__class__.__name__=='Caretaker']
        result=f"You have {len(self.workers)} workers"+'\n'
        result+=f"----- {len(keepers)} Keepers:"+'\n'
        result+="{}".format('\n'.join([repr(k) for k in keepers]))+'\n'

        result += f"----- {len(caretakers)} Caretakers:" +'\n'
        result += "{}".format('\n'.join([repr(k) for k in caretakers])) + '\n'
        result += f"----- {len(vets)} Vets:"+'\n'
        result += "{}".format('\n'.join([repr(k) for k in vets]))
        return result

# todo judge izobshto ne priema