class BinaryList:
    def __init__(self,arr,dataType=int):
        self.itemArr=arr
        self.arrSize=len(self.itemArr)
        self.dataType=dataType
        for j in self.itemArr:
            if type(j)!=dataType:
                print("not same type of data")
                exit()
        if self.itemArr[0] > self.itemArr[1]:
            print("not sorted")
            exit()
    def display(self):
        print(self.itemArr)
    def binarySearch(self,searchItem):
        beg=0
        end=self.arrSize-1
        while beg <= end:
            mid=(beg+end)//2
            if (searchItem == self.itemArr[mid]):
                print(f"index of {searchItem} is {mid}")
                return mid
            elif searchItem < self.itemArr[mid]:
                end=mid-1
                print(end)
            else:
                beg=mid+1
    def insertItem(self,pos,insertItem):
        if self.itemArr [pos-1] > insertItem:
             print("not allowed")
        else:
            self.itemArr.insert(pos,insertItem) 
            print("successfully inserted")
    def deleteItem(self,delItem):
        if delItem in self.itemArr:
            self.itemArr.remove(delItem)
            print("successfully deleted")

        else:
            print (f"{delItem} not found")

obj=BinaryList([1,2,3,4,5])
obj.binarySearch(5)
obj.insertItem(4,0)
obj.display()