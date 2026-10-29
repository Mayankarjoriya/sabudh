
from Task_1 import Person

class Employee(Person):
    counter = 0
    def __init__(
            self,
            name:str,
            age:int,
            gender:str,
            address:str,
            salary:float,
    ):
        super().__init__(name=name,age=age,gender=gender,address=address)

        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter}"

        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    @property
    def employee_count(self):
        return Employee.counter

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    def increase_salary(self, amount:float):
        if amount > 0:
            self.__salary += amount

    def decrease_salary(self, amount:float):
        if 0 < amount <= self.__salary:
            self.__salary -= amount

    def introduce(self):
        return f"Hello my name is {self.name} and i work as an employee"

