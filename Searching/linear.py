def linearS(a,key):
    for i in range(len(a)):
        if(a[i]==key):
            return i
print(linearS([1,2,3,4,5],1))