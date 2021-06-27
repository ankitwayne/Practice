n=input("Enter numbers of elements = ")
list=[]
for i in range(n):
 num=input("Enter element = ")
 list.insert(i,num)
print "maximum elements in the list = ",max(list)
print "minimum elements in the list = ",min(list)