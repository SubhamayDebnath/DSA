class SelectionSort:
    def __init__(self,arr,dataType=int):
        self.arr=arr
        self.dataType=dataType
        for i in self.arr:
            if(type(i)!=dataType):
                print("not same type of data")
                exit()
    def display(self):
        print(self.arr)
    def selectionSort(self):
        for j in range(len(self.arr)-1):
            for k in range(j+1,len(self.arr)):
                if self.arr[j] > self.arr[k]:
                    temp=self.arr[j]
                    self.arr[j]=self.arr[k]
                    self.arr[k]=temp
    def insertItem(self,pos,item):
        self.arr.insert(pos,item)
        print("successfully inserted")
    def deleteItem(self,delItem):
        self.arr.remove(delItem)
        print("successfully deleted")
               
obj=SelectionSort([3,7,1,4,5]);
obj.selectionSort()
obj.insertItem(2,89)
obj.display()
obj.selectionSort()
obj.deleteItem(89)
obj.display()