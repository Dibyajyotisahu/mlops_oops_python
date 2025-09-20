# initiate class
class Employee:
    # constructor
    def __init__(self):
        print("starting employee details")
        self.id="123"
        self.salary="50000"
        self.designation="Developer"
        print("employee details are set"  )

    #method
    def travel(self,destination):
        print("this travel function was called manually")
        print("employee is travelling to",destination)

# create object
emp=Employee()

#print attribute and call method
print(emp.id)
print(emp.travel("kolkata"))

emp.name="Dibyajyoti Sahu"
print(emp.name)
print(id(emp))

print(emp.__dict__)

print(type(emp))

