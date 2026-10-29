from Task_2 import Employee
from Task_1 import Person

class Teacher(Employee):
    counter =0
    def __init__(
            self,name: str,age: int,gender: str,address: str,salary: float,subjects: list = None):

        super().__init__(name=name,gender=gender,age=age,address=address,salary=salary)
        Teacher.counter +=1
        self.__teacher_id=f"Tec{Teacher.counter:02d}"

        self.subjects = subjects if subjects is not None else []

    def __del__(self):
        Teacher.counter -=1
        super().__del__()

    @property
    def teacher_id(self) -> str:
        return self.__teacher_id
    @property
    def teacher_count(self) -> int:
        return Teacher.counter

    def get_teacher_id(self) -> str:
        return self.__teacher_id

    def add_subject(self,subject:str) -> None:
        if subject not in self.subjects:
            self.subjects.append(subject)
            return f"Subject {subject} added"
        return f"Subject {subject} already exists"
    def remove_subject(self,subject:str) -> None:
        if subject not in self.subjects:
            self.subjects.remove(subject)

    def introduce(self):
        subjects_str = ", ".join(self.subjects)
        return f"My ID is {self.teacher_id} and I teach: {subjects_str}"
    @property
    def employee_id(self):
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute 'employee_id'"
        )
    def get_employee_id(self) -> str:
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute 'employee_id'"

        )


if __name__ == "__main__":
    print("Testing Person Class")
    print(f"Is age 20 adult? {Person.is_adult(age=20)}")
    print(f"Is age 15 adult? {Person.is_adult(age=15)}")

    print("\nTesting Employee")
    emp1 = Employee(name = 'Alice',age=30,gender='female',address='123, main street', salary=30000.00)
    emp2 = Employee(name='Mayank',age=31,gender='Male',address='Mansarovar,jaipur',salary=35000.00)

    print(f"employee 1: {emp1}")
    print(f"Employee greet: {emp1.greet(emp2)}")
    print(f"employee 1 introduce: {emp1.introduce()}")

#     getter
    print(f"ID employee 1: {emp1.employee_id}")
    print(f"ID employee 2: {emp2.employee_id}")
    print(f"Current Employee count: {Employee.counter}")

    print(f"employee 1 intial salary: {emp1.salary}")
    emp1.increase_salary(500)
    print(f"Employee 1 increased salry {emp1.salary}")
    emp1.decrease_salary(100)
    print(f"Employee 1 decresed salry {emp1.salary}")

    print("\nTesting Teacher Class")
    t1 = Teacher(
        name='John',
        age=40,
        address='125 main street',
        gender='Male',
        salary=40000,
        subjects=['Math','Science']
    )

    print(f"teacher-1 id: {t1.teacher_id}")
    print(f"teacher-1 introduce: {t1.introduce()}")

    t1.add_subject('English')
    print(f"Introduce after adding subject: {t1.introduce()}")

    t1.remove_subject('Science')
    print(f"After removing subject {t1.introduce()}")

    print(f"Total teachers: {Teacher.counter}")













