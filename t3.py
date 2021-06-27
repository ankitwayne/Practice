#Fibanacci series by python
n=input("Enter any term = ")
n1=0
n2=1
i=1
print n1,n2,
while i<=n-2:
 n3=n1+n2
 n1=n2
 n2=n3
 i=i+1
 print n3,
