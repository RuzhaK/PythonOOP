class DVD:
    _month_by_number={
        '1':'January',
        '2':'February',
        '3':'March',
        '4':'April',
        '5':'May',
        '6':'June',
        '7':'July',
        '8':'August',
        '9':'September',
        '10':'October',
        '11':'November',
        '12':'December'
    }
    def __init__(self,name, id, creation_year, creation_month,age_restriction):
        self.is_rented=False
        self.name=name
        self.id=id
        self.creation_year=creation_year
        self.creation_month=creation_month
        self.age_restriction=age_restriction

    @classmethod
    def from_date(cls,id: int, name: str, date: str, age_restriction: int):
        day,month,year,*rest=date.split(".")
        creation_month=cls._month_by_number[month]
        return cls(name, id,creation_year=int(year),creation_month=creation_month,age_restriction=age_restriction)
    def __repr__(self):
        status='rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
    def rent(self):
        self.is_rented=True
    def unrent(self):
        self.is_rented=False
