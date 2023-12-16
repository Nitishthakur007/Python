class Person:
    country = "india"

    def breath(self):
        print("I am breathing....")


class Employee(Person):
    company = "Microsoft"

    def breath(self):
        print("I am an employee so i am breathing...")


class programmer (Employee):
    company = "fiverr"

    def breath(self):
        print("i am a programmer so i am breathing....")


p = Person()
p.breath()
e = Employee()
print(e.company)
pr = programmer()
pr.breath()
print(pr.company)
print(pr.country)
