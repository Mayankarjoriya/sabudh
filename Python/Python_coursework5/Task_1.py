
import abc

class Person(abc.ABC):

    def __init__(self,name,age,gender,address):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self,other_person):
        return f"Hello {other_person.name}! My name is {self.name}"

    @abc.abstractmethod
    def introduce(self) -> str:
        pass

    @staticmethod
    def is_adult(age:int) -> bool:
        result = age >= 18
        return f"{result}"









