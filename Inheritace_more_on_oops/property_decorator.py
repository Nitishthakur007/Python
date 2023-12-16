class Employee:
    company = "campus"
    salary = 7000
    bonus = 1200

    @property
    def totalsalary(self):
        return self.salary + self.bonus

    @totalsalary.setter
    def totalsalary(self, val):
        self.bonus = val-self.salary


e = Employee()
print(e.totalsalary)
e.totalsalary = 8000
print(e.salary)
print(e.totalsalary)
print(e.bonus)
