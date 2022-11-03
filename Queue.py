class Queue(object):
    def __init__(self):
        self.myqueue = []
    
    def isEmpyty(self):
        return self.myqueue == []

    def enqueue(self,item):
        self.myqueue.insert(0,item)
    
    def dequeue(self):
        return self.myqueue.pop()
    
    def viewQueue(self):
        return self.myqueue
    
    def size(self):
        return len(self.myqueue)

q = Queue()

print(q.isEmpyty())
for i in range(11):
    q.enqueue(i)

print(q.viewQueue())

for i in range(q.size()):
    print(q.dequeue())

