#queue: enqueue and dequeue:
class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
class Queue:
    def __init__ (self):
        self.front=self.rear=None
    def Enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            dta=new_node.data
            print("enqueued when empty:",dta)
        else:
            self.rear.Next=new_node
            self.rear=new_node
            data=new_node.data
            print("enqueued:",data)
    def Dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp=self.front
            self.front=temp.Next
            deleted_item=temp.data
            del(temp)
            temp=None
            print(f"dequeued item from the queue is:{deleted_item}")
q=Queue()
q.Enqueue(30)
q.Dequeue()
q.Dequeue()
