def sod(n):
 sum=0
 while n>0:
  rem=n%10
  sum=sum+rem
  n=n/10
 print "Sum of digit =  ",sum
a=input("Enter a number = ")
sod(a)
