def bubbleSort(a):
    n=len(a)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if( a[j] > a[j+1] ):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
a=[1,44,6,4,3,9,8,0]
bubbleSort(a)
print(a)