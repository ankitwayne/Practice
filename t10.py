n=input("Enter no of elements = ")
list=[]
for i in range(0,n):
 e=input()
 list.insert(i,e)
print "Display all elements \n"
for e in list:
 print e
 sum=sum+i
average=sum/len(list)
print "sumof list = ",sum
print "average of list = ",average