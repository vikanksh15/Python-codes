class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None  #adding tail to our linkedList
    
    
a = Node(1)  #adding a new node
b = Node(2) 
c = Node(3)
a.nextnode = b #assigning reference to our node
b.nextnode  = c  

print(a.value)
print(a.nextnode)
print(c.value)
print(c.nextnode)



# d = Node(4)
# c.nextnode = d
# print(d.nextnode)
# a1 = Node(0)
# a1.nextnode = a
# print(a1.value)
# print(a1.nextnode)