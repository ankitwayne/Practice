x = input("Enter any string: ")
if x == 's':
    exit();
else:
    w = x;
    vow = ('a', 'e', 'i', 'o', 'u');
    for s in x.lower():
        if s in vow:
            print("Vowels removed are : ",s);
            w = w.replace(s,"");
    print("New string after successfully removed all the vowels:");
    print(w);