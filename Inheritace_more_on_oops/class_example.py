class School:
    name = "Dps"
    location = "Delhi"

    def student(self):
        print(f"Good morning {self.Name}")
        print(f"here is number {self.number}")


harry = School()
harry.Name = "harry"
harry.number = 656465465
print(harry.name)
harry.student()


ajey = School()
ajey.Name = "ajey"
ajey.number = 5566
print(ajey.location)
ajey.student()
