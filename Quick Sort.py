def partition(arr, beg, end):
    a=(beg-1)
    mid=arr[end]
    for i in range(beg, end):
        if arr[i]<=mid:
            a=a+1
            arr[a],arr[i]=arr[i],arr[a]
    arr[a+1],arr[end]=arr[end],arr[a+1]
    return (a+1)
def quick(arr, beg, end):
    if beg<end:
       mid=partition(arr,beg, end)
       quick(arr,beg, mid-1)
       quick(arr, mid+1, end)


a=[2,8,6,4,9,3,1]
print("Given array is: ",a)
quick(a,0,len(a)-1)
print("Sorted array is: ",a)
a=[9,4,6,2,7,8,5,3,1]
print("Given elements are : ",a)
quick(a,0,len(a)-1)
print("Sorted array is: ",a)
