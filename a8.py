n= input("Enter a number = ")
temp=n
sum=0
while n>0:
 rem=n%10
 sum=sum+(rem*rem*rem)
 n=n/10
if temp==sum:
 print "Is a Armstrong number"
else:
 print "Not a Armstrong number"