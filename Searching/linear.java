public class linear{
    public int linearS(int a[],int key)
    {
        for(int i=0;i<a.length;i++)
        {
            if(a[i]==key)
            {
                return i;
            }
        }
        return -1;
    }
    public static void main(String args[])
    {
        linear l = new linear();
        int a[]={1,2,3,4,5};
        int key=5;
        System.out.print(l.linearS(a,key));
    }
}