class Employee:
    company = "Visa"
    Ecode = 120


class Freelancer:
    company = "Fiverr"
    level = 2

    def upgradelevel(self):
        self.level = self.level+1


class programmer(Employee, Freelancer):
    name = "rohit"


p = programmer()
p.upgradelevel()
print(p.company)
print(p.level)
