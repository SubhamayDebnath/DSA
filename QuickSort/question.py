class QuickSort:
    def __init__(self,arr,dataType=int):
        self.arr=arr
        self.dataType=dataType
        for i in self.arr:
            if(type(i)!=dataType):
                print("not same type of data")
                exit()
    def display(self):
        print(self.arr)
    def quickSort(self):
        