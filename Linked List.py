
class Node:
    def __init__(self,data=None):
        self.data= data
        self.next= None   
        
class singlelist:
    def __init__(self):
        self.head= None
        self.tail= None
    
    def addbeg(self, data):
        node=Node(data)
        if self.head== None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
            
    def addaft(self,node,new_data):
        if node is None:
            print("Node is absent")
            return
        new_node=Node(new_data)
        new_node.next=node.next
        node.next=new_node
            
    def addend(self, data):
        node=Node(data)
        if self.head== None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
            
    def delbeg(self):
        if self.head==None:
            print("List is Empty")
        elif self.head==self.tail:
            t=self.head
            self.head =self.tail=None
            del t
        else:
            t=self.head
            self.head=t.next
            del t
      
    def delend(self):
        if self.head==None:
            print("List is Empty")
        elif self.head==self.tail:
            t=self.head
            self.head =self.tail=None
            del t
        else:
            t=self.head
            while t.next!=self.tail:
                t=t.next
            t.next=None
            self.tail=t
            del t
            
    def traverse(self):
        t=self.head
        while t!=None:
            if t.next!=None:
                print(t.data,end="->")
            else:
                print(t.data)
            t=t.next
l=singlelist()
l.addbeg(10)
l.addbeg(20)
l.addbeg(30)
l.addbeg(40)
print("List after Addbeg operations :")
l.traverse()
l.addend(500)
l.addend(100)
print("List after Addend operations :")
l.traverse()
l.delbeg()
print("List after delbeg operations :")
l.traverse()
l.delend()
print("List after delend operations :")
l.traverse()