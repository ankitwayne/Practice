def selectsort(arr):
    for i in range(len(arr)-1):
        mi=i
        for j in range(i+1,len(arr)-1):
            if arr[mi]>arr[j]:
                mi=j
        arr[i],arr[mi]=arr[mi],arr[i]
        
l=[3,5,2,8,6]
print("Given elements are :",l)
selectsort(l)
print("Sorted elements are : ",l)


l=[13,15,12,18,16]
print("Given elements are :",l)
selectsort(l)
print("Sorted elements are : ",l)