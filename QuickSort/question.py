def quickSort(arr,left,right):
    if left < right:  
        q=quick(arr,left,right)
        quickSort(arr,left,q-1)  
        quickSort(arr,q+1,right)     
def quick(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i < j:
        while i < j and arr[i] < pivot:
            i+=1
        while j > i and arr[j] >=pivot:
            j-=1
        if i < j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    if arr[i] > pivot:
        temp=arr[i]
        arr[i]=arr[right]
        arr[right]=temp
    return i
arr=[22,11,88,45,89,1]
quickSort(arr,0,len(arr)-1)
print(arr)

