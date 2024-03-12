class BubbleSort:
    def __init__(self,arr,dataType=int):
        self.arr=arr
        for i in self.arr:
            if type(i)!=dataType:
                print("not same type of data")
                exit()
    def display(self):
        print(self.arr)
    def bubbleSort(self):
        for j in range(1,len(self.arr)):
            for k in range(len(self.arr)-j):
                if self.arr[k] > self.arr[k+1]:
                    temp=self.arr[k]
                    self.arr[k]=self.arr[k+1]
                    self.arr[k+1]=temp
    def insertItem(self,pos,item):
        self.arr.insert(pos,item)
        print("successfully inserted")
    def deleteItem(self,delItem):
        if delItem in self.arr:
            self.arr.remove(delItem)
            print("successfully deleted")
        else:
            print (f"{delItem} not found")
obj=BubbleSort([3,7,1,4,5])
obj.bubbleSort()
obj.display()
obj.insertItem(0,99)
obj.display()
obj.bubbleSort()
obj.display()
obj.deleteItem(99)
obj.display()
    
