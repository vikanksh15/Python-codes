from msvcrt import kbhit


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
    
    @classmethod
    def alternative_const(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))


harry = Item('harry',255,"Teacher")
rohan = Item('Rohan',455,"Student")
karan = Item.alternative_const("karan-420-Berozgar")


print(harry.printdetails())
print(rohan.printdetails())
print(karan.printdetails())
