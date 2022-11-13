# #polymorphism : Ability to take various forms
# print(5+6) #here "+" operator is used to add two numbers
# print("5"+"6") #here same operator is used to concatenate two string

class Cat:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    
    def info(self):
        return f"I am a Cat and My name is {self.name} and I am {self.age} years old"
    
    def make_sound(self):
        return "Meow"

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"I am a Dog and My name is {self.name} and I am {self.age} years old"
    
    def make_sound(self):
        return "Bark"

cat1 = Cat("Julia",5)
dog1 = Dog("Bruno",8)

for animal in (cat1,dog1):
    print(animal.make_sound())
    print(animal.info())
    print(animal.make_sound(),'\n')
