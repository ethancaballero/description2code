import java.util.Scanner;
 
 class Main {
 
    public static void main(String[] args) throws Exception {
 
        Scanner sc = new Scanner(System.in);
        String s = null;
        int result = 0;
        int flag = 0;
 
        while (!(s = sc.next()).equals("~")) {
 
            int i = 0;
           
            if (!s.equals("#")) {
                if (s.equals("0")) {
                    flag = 1;
                } else if (s.equals("00")) {
                    flag = 0;
                } else {
                    for (i = 2; i < s.length(); i++) {
                        result = result*2 + flag;
                    }
                }
            } else {
                System.out.println(result);
                 flag = 0;
                 result = 0;
            }
 
        }
 
    }
}