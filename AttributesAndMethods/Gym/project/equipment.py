class Equipment:
    _id=1
    def __init__(self,name):
        self.name=name
        self.id=self._id
        self.__class__._id+=1
        # incremented
    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    # @classmethod
    # def get_next_id(cls):
    #     return cls._id

    @staticmethod
    def _get_next_id(cls):
        return cls._id
    get_next_id=_get_next_id