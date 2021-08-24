##python Flow control

#python if-else
print("if-else condition..")
num = 8
if num >=0 : 
    print("Given number is positive")
elif num == 0:
    print("Given number is 0")
else:
    print("Given number is negative")

#python for loop
print("\n")
print("for loop..")
numbers = [1,2,3,4,6,8]

sum = 0
print("Elements in list are...")
for i in numbers:
    print(i)
    sum = sum+ i
print("Sum of all elements of list is",sum)

#range() function
print("\n")
print("range() function..")
print(range(10))
print(range(1,10))
print(list(range(1,10)))
print(list(range(1,10,2)))

#python while loop
print("\n")
print("while loop..")
i = 0
while numbers[i] != 8 :
    print(numbers[i])   
    i += 1


#python break statement 
print("\n")
s = "difference between break and continue is....."
snew = s.split()
print(s)
print("break example..")
for i in snew:
    if i == "break":
        break
    print(i)

#python continue statement
print("\n")
print("continue example..")
for i in snew :
    if i == "break":
        continue
    print(i)

#python pass
print("\n")
'''pass is just
a placeholder for
functionality to be added later'''
def passexample(i):
    pass