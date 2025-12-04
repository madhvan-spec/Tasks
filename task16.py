class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"


class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)  
        self.employee_id = employee_id
        self.position = position

    def work(self):
        return f"{self.name} is working as a {self.position}."

    def introduce(self):
        print (f"Hi, I'm {self.name}, age {self.age}, "
                f"Employee ID {self.employee_id}, working as a {self.position}")

    def __str__(self):
        return (f"Employee(name='{self.name}', age={self.age}, "
                f"employee_id='{self.employee_id}', position='{self.position}')")


p1 = Person("Madhvan","21")
e1 = Employee(p1.name,p1.age,1,"Software Engineer Intern")
p1.introduce()
print(p1)
e1.work()
e1.introduce()
print(e1)
