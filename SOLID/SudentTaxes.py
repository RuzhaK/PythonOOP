from abc import ABC,abstractmethod
class StudentTaxes(ABC):
    def __init__(self,name, semester_fee,average_grade):
        self.average_grade = average_grade
        self.semester_fee = semester_fee
        self.name = name
    @abstractmethod
    def get_discount(self):
        pass
        # if self.average_grade>=5:
        # #     return self.semester_fee*0.4
        # # elif self.average_grade>=4:
        # #     return self.semester_fee*0.3


class ExcellentStudent(StudentTaxes):
    def get_discount(self):
        return self.semester_fee*0.4

class AverageStudent(StudentTaxes):
    def get_discount(self):
        return self.semester_fee * 0.3