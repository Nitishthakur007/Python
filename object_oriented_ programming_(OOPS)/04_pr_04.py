class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"the value of {self.num} is {self.num*self.num}")

    def squareRoot(self):
        print(f"the value of {self.num} is {self.num**0.5}")

    def cube(self):
        print(f"the value of {self.num} is {self.num**3}")

    @staticmethod
    def greet():
        print("Welcome to the best calculator")


a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()
