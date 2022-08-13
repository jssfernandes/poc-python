import json

class Pokemon:
    id:int
    name:str
    height:int
    weight:int

    # def __init__(self, id, name, height, weight):
    #     self.id = id
    #     self.name = name
    #     self.height = height
    #     self.weight = weight

    def __str__(self) -> str:
        # return f'id: {self.id}, name: {self.name}'
        return json.dumps(self.__dict__)

