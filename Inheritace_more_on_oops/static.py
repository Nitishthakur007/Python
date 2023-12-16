class Employee:
    Name = "Google"
    location = "delhi"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp_1 = Employee("ajey", 1000)
print(emp_1.name)
