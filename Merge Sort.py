def mergesort(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]
        
        mergesort(l)
        mergesort(r)
        
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
            
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1
                    
a=[12,13,15,19,14,16]
print("Given elements are : ",a)
mergesort(a)
print("Sorted elements are : ",a)

a=[9,4,6,2,7,8,5,3,1]
print("Given elements are : ",a)
mergesort(a)
print("Sorted elements are : ",a)