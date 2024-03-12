def mergeSort(arr1,arr2,dataType=int):
    i=0
    j=0
    k=0
    c=[]
    arr1Len=len(arr1)
    arr2Len=len(arr2)
    for m in arr1:
        if type(m) != int:
            print("not same type of data")
            exit()
    for n in arr1:
        if type(n) != int:
            print("not same type of data")
            exit()
    while i < arr1Len and j < arr2Len:
        while arr1[i] < arr2[j]:
            c[k]=arr1[i]
            i+=1
            k+=1
        while arr2[j] < arr1[i]:
            c[k]=arr2[j]
            j+=1
            k+=1
        # while i < arr1Len:
        #     c[k]=arr1[i]
        #     k+=1
        #     i+=1
        # while j < arr2Len:
        #     c[k]=arr2[j]
        #     k+=1
        #     j+=1
    print(c)
mergeSort([10,30,35,99],[5,40,82])