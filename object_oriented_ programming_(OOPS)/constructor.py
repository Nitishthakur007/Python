class Employee:
    company = "Google"

    def __init__(self, salary, subunit):
        self.salary = salary
        self.subunit = subunit

    def getdetails(self):
        print(f"salary is {self.salary}")
        print(f"salary is {self.subunit}")

        print("is created")


harry = Employee(1000, "youtube")
harry.getdetails()
