import java.util.Scanner;

public class decimalToBin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] bin = new int[16];
        for(int i=15;i>=0;i--)
        {
            if((n & (1<<i)) == (1<<i))
            {
                System.out.print(1+" ");
                bin[i]=1;
            }
            else{
                System.out.print(0+" ");
                bin[i]=0;
            }
        }
        for(int i=15;i>=0;i--)
        {
            // System.out.print(bin[i]+" ");
        }
    }
}
