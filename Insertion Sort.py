def insertsort(arr):
    for i in range(1,len(arr)):
        data=arr[i]
        j=i-1
        while j>=0 and data<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=data

l=[5,6,8,0,4,9]
print("Given elements are :",l)
insertsort(l)
print("Sorted elements are : ",l)


l=[11,16,12,14,22,19]
print("Given elements are :",l)
insertsort(l)
print("Sorted elements are : ",l)