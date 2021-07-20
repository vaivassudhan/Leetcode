def BinaryS(a,key):
    n=len(a)
    l=0
    r=n-1
    while(l <= r):
        mid = (l+r)//2
        if( a[mid] == key ):
            return mid
        elif( key < a[mid]):
            r = mid - 1 
        else:
            l = mid + 1
    return -1

a=[1,2,3,4,5,6,7,8,9,10]
print(BinaryS(a,10))