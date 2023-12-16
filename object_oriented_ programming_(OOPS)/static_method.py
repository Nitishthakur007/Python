class Employee:
    company = "Google"

    def getsalary(self, signature):
        print(
            f"salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning sir")

    @staticmethod
    def time():
        print("time is 9am")


harry = Employee()
harry.salary = 100000
harry.getsalary("thanks")  # Employee.getsalary(harry)
harry.greet()
harry.time()
