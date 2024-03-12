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
        pivot=0
        right=len(self.arr)
        left=1
        while True:
            while self.arr[pivot] <= self.arr[right] and left <=right:
                right=right+1
                if self.arr[pivot] >= self.arr[right]:
                    temp=self.arr[pivot]
                    self.arr[pivot]=self.arr[right]
                    self.arr[right]=temp
                if left >right:
                    return pivot
            while self.arr[pivot] >= self.arr[left] and left <=right:
                left=left+1
                if self.arr[pivot] >= self.arr[left]:
                    temp=self.arr[pivot]
                    self.arr[pivot]=self.arr[left]
                    self.arr[left]=temp
                if left >right:
                    return pivot
        