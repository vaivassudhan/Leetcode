public class bubbleSort {

    public void bsort(int a[])
    {
        int n=a.length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n-i-1;j++)
            {
                if(a[j]>a[j+1])
                {
                    a[j+1]=a[j]+a[j+1];
                    a[j]=a[j+1]-a[j];
                    a[j+1]=a[j+1]-a[j];
                }
            }
        }
        
    }
    public static void main(String args[])
    {
        int a[]={1,5,4,6,3,7,2};
        bubbleSort bs = new bubbleSort();
        bs.bsort(a);

        for(int i=0;i<a.length;i++)
        {
            System.out.print(a[i]+" ");
        }
    }
}
