# from unicodedata import name


# public - Just variable name
# protected - _name
# private - __name
class MyClass():
    principal = "Dumbeldore"
    _vicepc = 'Snape'
    __headboy = 'Harry'
    def __init__(self,number,subject):
        self.number = number
        self.section = subject
        
    
    def printdetails(self):
        return f"This is class {self.number} and subject is {self.section}"

a1 = MyClass(1,'Potions')
print(MyClass.principal,'is the Global Variable and Headmaster')
print(MyClass._vicepc,'is the protected variable and Vice pc')
print(MyClass._MyClass__headboy,"is the private class and Head Boy")
print(a1.printdetails())

