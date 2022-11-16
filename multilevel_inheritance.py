class Dad:
    age = 80
    speed = 20
    Experience = 100
    def myexp(self):
        return f"I got {self.Experience} experience"

class son(Dad):
    age = 30
    speed = 50
    level = 'average'
    def mylevel(self):
        return f"My level is {self.level}, you don't wanna mess"

class grandson(son):
    age = 20
    speed = 100
    rank = 'newbie'
    def __str__(self):
        return f"I inherit all"

ben = Dad()
Patrice = son()
alan = grandson()

# print(alan.speed)
# print(alan.Experience)
# print(alan.level)
print(alan)
print(Patrice.myexp())
print(alan.mylevel())