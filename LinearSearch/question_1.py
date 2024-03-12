class LinearList:
    def __init__(self,arr,dataType=int):
        self.itemArr=arr
        self.arrSize=len(self.itemArr)
        self.dataType=dataType
        for j in self.itemArr:
            if type(j)!=dataType:
                print("not same type of data")
                exit()
    def display(self):
        print(self.itemArr)
    def linearSearch(self ,searchItem):
        for i in range(self.arrSize):
            if searchItem == self.itemArr[i]:
                print(f"index of {searchItem} is {i}")
                return i
        else:
            print(f"{searchItem} is not found")
    def insertItem(self,pos,insertItem):
        self.itemArr.insert(pos,insertItem)
        print("successfully inserted")
    def deleteItem(self,delItem):
        self.itemArr.remove(delItem)
        print("successfully deleted")
obj=LinearList([1,3,9,8,7],int)
obj.linearSearch(9)
obj.insertItem(0,99)
obj.deleteItem(1)
obj.display()