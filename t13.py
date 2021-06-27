def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y   
def div(x,y):
 return x/y
print "Enter operation : "
print "1.Addition : "
print "2.Substraction : "
print "3.Multiplication : "
print "4.Division : "
choice=input("Enter your choice(1/2/3/4): ", )
n1=input("Enter first number : ")
n2=input("Enter second number : ")
if choice=='1':
 print add(n1,n2)
elif choice=='2':
 print sub(n1,n2)
elif choice=='3':
 print mul(n1,n2)
elif choice=='4':
 print div(n1,n2)
else:
 print "invalid input"