class Person:
    country = "india"

    def breath(self):
        print("I am breathing....")


class Employee(Person):
    company = "Microsoft"

    def breath(self):
        super().breath()
        print("I am an employee so i am breathing...")


class programmer (Employee):
    company = "fiverr"

    def breath(self):
        super().breath()
        print("i am a programmer so i am breathing....")


p = Person()
p.breath()

e = Employee()
e.breath()

pr = programmer()
pr.breath()
