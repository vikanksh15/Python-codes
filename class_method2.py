class Item(object):
    no_of_leaves = 10

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def printdetails(self):
        return f"Name : {self.name}, Salary : {self.salary}, Role : {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

harry = Item('harry',255,"Teacher")
rohan = Item('Rohan',455,"Student")

Item.change_leaves(50)

print(rohan.no_of_leaves)