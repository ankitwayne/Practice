for i in range(1,101):
 if i>1:
  for num in range(2,i):
   if (i%num)==0:
    break
  else:
   print(i) 
