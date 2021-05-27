import math
class Integer:
    def __init__(self, value:int):
        self.value=value
    @classmethod
    def from_float(cls,value):
        if isinstance(value,float):
            return cls(math.floor(value))
        return "value is not a float"
    @classmethod
    def from_roman(cls,value) :
        rom_val = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
                          "V": 5, "IV": 4, "I": 1}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls,value) :
        try:
            if not isinstance(value,str):
                raise ValueError('Not an instance of string')
            return Integer(int(value))

        except ValueError:
            return "wrong type"

    def add(self,integer:int) :
        if not isinstance(integer,Integer):
            return "number should be an Integer instance"
        return self.value+integer.value

first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
