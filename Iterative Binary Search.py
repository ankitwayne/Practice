def binasearch(list3,key):
    l,h,m=0, len(list3)-1,0
    while l<=h:                      # [l,h]= lower element, higher element
        m=(h+l)//2
        if list3[m]<key:             # [m]= middle element
            l=m+1
        elif list3[m]>key:
            h=m-1
        else:
            return m
    return -1

list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(list3)
key=int(input("Input number from below list to search its index: "))
loc=binasearch(list3,key)
print("The Index of element is :-",loc)12
