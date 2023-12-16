class Employee:
    company = "google"
    location = "India"

    def details(self):
        print("this is an employee")


class programmer(Employee):
    salary = 100


a = Employee()
print(a.company)
a.details()

b = programmer()
print(b.company)
print(b.salary)
