#Name : Ankit Mishra
#Roll No : 2000320109002
#Class : CSE2-A2
#Practical Name : Program for Linear Search

def linsearch(list,key):
    for i in range(len(list)):
        if list[i]==key:
            return i
    return -1

list=[12,35,54,18,65,45,17,66]
print(list)
x=int(input("Input number from below list to search its index: "))

loc=linsearch(list,x)
print("The Index of element is :-",loc)