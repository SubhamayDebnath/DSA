def quick(arr,left,right):
    pivot=left-1
    while True:
        while arr[pivot] <= arr[right] and left <= right:
            right = right -1
            if arr[pivot] >=  arr[right]:
                temp=arr[pivot]
                arr[pivot]=arr[right]
                arr[right]=temp
                right=right-1
            if left >right:
                return pivot
        while arr[pivot] >= arr[left] and left <= right:
            left = left+1
            if arr[pivot] <=  arr[left]:
                temp=arr[pivot]
                arr[pivot]=arr[left]
                arr[left]=temp
                left=left+1
            if left > right:
                return pivot
def quickSort(arr,left,right):
    if left <= right:
        pi=quick(arr,left,right)
        quick(arr,left,pi-1)
        quick(arr,pi+1,right)

arr=[23,54,7,8,9,23,90,69]
n=len(arr)-1
quickSort(arr,0,n)
print(arr)