#to find no of year days week by given no of days
d= input("Enter Number of Days = ")
y=d/365
w=d%365/7
d=(d%365)%7
print "year : ",y
print "week : ",w
print "days : ",d
