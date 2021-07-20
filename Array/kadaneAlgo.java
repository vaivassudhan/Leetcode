public class kadaneAlgo {
    public int maxSum(int a[])
    {
        int global_max = a[0];
        int local_max = 0;
        for(int i=0;i<a.length;i++)
        {
            local_max += a[i];
            if(local_max > global_max)
            {
                global_max=local_max;
            }
            if(local_max < 0){
                local_max=0;
            }
        }
        return global_max;
    }
    public static void main(String args[])
    {
        int a[]={4,-1,2,1};
        kadaneAlgo ka = new kadaneAlgo();
        System.out.print(ka.maxSum(a));
    }
}
