def primnum(a,b):
    for i in range(a, b+ 1):
       # all prime numbers are greater than 1
       if i > 1:
           for j in range(2, i):
               if (i % j) == 0:
                   break
           else:
               print(i)
a=int(input("Enter Begining Number : "))
b=int(input("Enter Begining Number : "))
primnum(a,b)
