public class reverseRec {
    public String reverse(String s)
    {
        if((s.length())==1 || s=="")
        {
            return s;
        }
        return reverse(s.substring(1))+(s.charAt(0));

    }
    public static void main(String[] args) {
        reverseRec rc= new reverseRec();
        System.out.println(rc.reverse("olleH"));

    }
}
