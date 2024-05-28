class Node:
    def __init__(self,value):
        self.Info=value
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.start=None
    def insertAtLast(self,value):
        n=Node(value)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.next != None:
                temp=temp.next
            temp.next=n
    def traverse(self):
        n=self.start
        while n!=None:
            print(n.Info)
            n=n.next
    def insertAtbegining(self,num):
        n=Node(num)
        n.next=self.start
        self.start=n
    def deleteLastNode(self):
        temp=self.start
        while temp.next != None:
            prev=temp
            temp=temp.next
        del temp 
        prev.next=None
    def insertAfterSpecificItem(self,item,position):
        n=Node(item)
        temp=self.start
        while temp.Info != position:
            temp=temp.next
        n.next=temp.next
        temp.next=n
    def deleteSpecificItem(self,position):
        temp=self.start
        while temp.Info != position:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        del temp
sl=SingleLinkedList()
sl.insertAtLast(20)
sl.insertAtLast(2)
sl.insertAtLast(50)
sl.insertAtLast(80)
sl.insertAtLast(87)
print("traverse 1")
sl.traverse()
sl.insertAtbegining(99)
print("traverse 2")
sl.traverse()
sl.deleteLastNode()
print("traverse 3")
sl.traverse()
sl.insertAfterSpecificItem(34,2)
print("traverse 4")
sl.traverse()
sl.deleteSpecificItem(34)
print("traverse 5")
sl.traverse()