class Mymath:
 def fact(self,n):
  if n==1 or n==0:
   return 1
  else:
   return n*self.fact(n-1)
math=Mymath()
n=input("Enter a number : ")
print "Factorial is : ",math.fact(n)