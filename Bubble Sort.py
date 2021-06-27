def bubblesort(list):
    key=len(list)
    for i in range(key):
        for j in range(0,key-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

list1=[12,45,16,52,3,14,25,31,29]
x=bubblesort(list1)
print(list1)



list2=[99,45,62,33,44,75,82,31,51,64]
y=bubblesort(list2)
print(list2)