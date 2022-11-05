#Doubly linked list implementation
class node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = node(1)
b = node(2)
c = node(3)
a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b