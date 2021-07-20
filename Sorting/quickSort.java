public class quickSort {
    public void swap(int a[], int i, int j)
    {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
    public int partition(int a[], int low, int high)
    {
        int i = low - 1;
        for ( int j=low; j<high ; j++)
        {
            if( a[j] < a[high] )
            {
                i++;
                swap(a, i, j);
            }
        }
        swap(a, i+1, high);
        return i+1;
    }
    public void qSort(int a[], int low, int high)
    {
        if(low < high)
        {
            int pi = partition(a, low, high);
            qSort(a, pi+1 , high);
            qSort(a, low, pi-1);
        }

    }
    public static void main(String args[])
    {
        int a[] = {100,-23,234,5,43,433};
        quickSort qs = new quickSort();
        qs.qSort(a, 0 ,a.length-1);
        for(int i=0;i<a.length;i++)
        {
            System.out.print(a[i]+" ");
        }
    }
}
