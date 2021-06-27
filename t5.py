# to find a prime number
num=input("Enter a  number = ")
i=1
c=0
while i<=num:
 if num%i==0:
  c=c+1
 i=i+1
if c==2:
 print "Prime Number"
else:
 print "Not Prime Number"
 