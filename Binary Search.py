#Name : Ankit Mishra
#Roll No : 2000320109002
#Class : CSE2-A2
#Practical Name : Program for Recursive Binary Search

def binsearch(list2,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if list2[mid]==key:
            return mid
        elif list2[mid]>key:
            return binsearch(list2, low, mid-1, key)
        else:
            return binsearch(list2, mid+1, high, key)
    else:
        return -1
    
list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(list2)
key=int(input("Input number from below list to search its index: "))
loc=binsearch(list2,0,len(list2)-1, key)
print("The Index of element is :-",loc)