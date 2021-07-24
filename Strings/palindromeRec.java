public class palindromeRec {
    public boolean recursion(String s)
    {
        if(s.length() == 0 || s.length()==1)
        {
            return true;
        }
        if(s.charAt(0) == s.charAt(s.length()-1))
        {
            return recursion(s.substring(1, s.length()-1));
        }
        return false;
    }
    public static void main(String[] args) {
        palindromeRec rc=new palindromeRec();
        System.out.println(rc.recursion("madan"));
    }
}
