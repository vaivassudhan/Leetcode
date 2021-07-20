def partition(a,low,high):
    i = low-1 
    for j in range(low,high):
        if( a[j] < a[high]):
            i+=1
            a[i],a[j] = a[j],a[i]
    a[high],a[i+1]=a[i+1],a[high]
    return i+1

def quickSort(a,low,high):
    if(low < high):
        pi = partition(a,low,high)
        quickSort(a,low,pi-1)
        quickSort(a,pi+1,high)

a=[5,4,9,12,22,3,7,1000,-90]
quickSort(a,0,len(a)-1)
print(a)