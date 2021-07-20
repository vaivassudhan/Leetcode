def selectionSort(a):
    n=len(a)
    min_index=0
    for i in range(n):
        for j in range(i+1,n):
            if ( a[j] < a[min_index] ):
                min_index = j
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp
a=[9,100,28,983,4,5]
selectionSort(a)
print(a)