class Employee:
    no_of_leaves = 10

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printdetails(self):
        return f"Employee's name is {self.name}; Age is {self.age}"
    

class Programmer(Employee):
    no_of_holiday = 60
    
    def __init__(self,name,age,role):
        self.name = name 
        self.age = age
        self.role = role
    
    def printabout(self):
        return f"Employee's name is {self.name}; Age is {self.age}; Role is {self.role}"

Rupesh = Programmer("Rupesh",20,"SDE")
print(Rupesh.printabout())
print(Rupesh.no_of_holiday)