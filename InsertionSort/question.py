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
    def InsertionSort(self):
        for k in range(1,len(self.arr)):
            item=self.arr[k]
            pos=k-1
            while item < self.arr[pos] and pos > len(self.arr):
                self.arr[pos+1]=self.arr[pos]
                pos-+1
            self.arr[pos+1]=item
obj=InsertionSort([9,3,1,8,7],int)
obj.InsertionSort()
obj.display()