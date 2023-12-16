class Employee:
    company = "camelin"
    salary = 100
    location = "delhi"

    @classmethod
    def changelocation(cls, locat):
        cls.location = locat


e = Employee()
print(e.salary)
e.changelocation("hyderabad")
print(e.location)


class Railwayform:
    Formtype = "Railway form"

    def data(self):
        print(f"name is {harrysapplication.name}")
        print(f"train name is {self.train}")
        print(f"and ticket is {self.ticket}")


harrysapplication = Railwayform()
harrysapplication.name = "Harry"
harrysapplication.train = "Rajdhani Express"
harrysapplication.ticket = "confirmed"
harrysapplication.data()
