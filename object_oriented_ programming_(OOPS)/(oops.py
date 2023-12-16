class Employee:
    company = "Google"
    location = "Hyderabad"


harry = Employee()
Employee.location = "mumbai"        # this will overwrite
print(harry.location)
print(harry.company)
