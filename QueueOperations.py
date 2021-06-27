class queue:
    def __init__(self,size):
        self.queue=[]
        self.size=size
    def isfull(self):
        return len(self.queue)==self.size
    def isempty(self):
        self.isempty==[]
    def enqueue(self,elem):
        if(self.isfull()!=True):
            return self.queue.insert(0,elem)
        else:
            print("Queue is Full")
    def dequeue(self):
        if(self.isempty()!=True):
            return self.queue.pop()
        else:
            print("Queue is Empty")
q=queue(9)

q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print("Queue formed after enque operation :",q.queue)
print("Deleted Item is :",q.dequeue())
print(q.queue)
