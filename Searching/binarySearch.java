public class binarySearch {
    public int binaryS(int a[],int key)
    {
        int l=0;
        int r=a.length-1;
        while(l<=r)
        {
            int mid=(l+r)/2;
            if(a[mid]==key)
            {
                return mid;
            }
            else if(key<a[mid])
            {
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return -1;
    }
    public int binaryRec(int a[],int l ,int r, int key)
    {
        if(r >= l)
        {
            int mid = l + (r-l) / 2;
            if(a[mid]==key)
            {
                return mid;
            }
            if(a[mid] > key){
                return binaryRec(a, l, mid-1, key);
            }
            return binaryRec(a,mid+1,r, key);
            
        }
        return -1;
    }
    public static void main(String args[])
    {
        int a[]={1,2,3,4,5};
        int n=5;
        int key=2;
        binarySearch bs=new binarySearch();
        System.out.println("Binary Search using loops "+bs.binaryS(a, key));
        System.out.println("Binary Search using recurssion "+bs.binaryRec(a,0,n-1, key));

    }
}
