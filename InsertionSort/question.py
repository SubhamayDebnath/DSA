class InsertionSort:
    def __init__(self,arr,dataType=int):
        self.arr=arr
        self.dataType=dataType
        for i in self.arr:
            if(type(i)!=dataType):
                print("not same type of data")
                exit()
    def display(self):
        print(self.arr)
    def insertionSort(self):
        for k in range(1,len(self.arr)):
            item=self.arr[k]
            pos=k-1
            while item < self.arr[pos] and pos >=0:
                self.arr[pos+1]=self.arr[pos]
                pos=pos-1
            self.arr[pos+1]=item
    def insertItem(self,pos,item):
        self.arr.insert(pos,item)
        print("successfully inserted")
    def deleteItem(self,delItem):
        if delItem in self.arr:
            self.arr.remove(delItem)
            print("successfully deleted")
        else:
            print (f"{delItem} not found")
           
obj=InsertionSort([9,3,1,8,7],int)
obj.display()
obj.insertionSort()
obj.display()
obj.insertItem(0,99)
obj.display()
obj.insertionSort()
obj.display()
obj.deleteItem(99)
obj.display()
