# a = 1
# print(str(a)+'11')

class CustomizedInteger:
    def __init__(self, integer):
        self.integer = integer
    
    def __repr__(self):#However in Python shell __repr__ is given preferance
        return f'CustomizedInteger({self.integer})'

    def __str__(self):#python prioritize __str__ over __repr__
        if self.integer == 3:
            return "Three"
    
    def __add__(self,other):
        return self.integer + other.integer

int1 = CustomizedInteger(3)
int2 = CustomizedInteger(7)

print(int1+int2)
