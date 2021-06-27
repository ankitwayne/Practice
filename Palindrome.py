def palindrome(x):
    w = ""
    for i in x:
        w = i + w
 
    if (x == w):
        print("Yes, it is a palindrome")
    else:
        print("No, it isn't a palindrome")
        
y = input("Enter the String : ")
palindrome(y)