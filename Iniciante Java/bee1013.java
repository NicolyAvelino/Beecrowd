// 1013 - O Maior
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int a,b,c,mAB, resp;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        
        mAB = (a + b + Math.abs(a-b))/2;
        resp = (mAB + c + Math.abs(mAB-c))/2;
        
        System.out.printf("%d eh o maior\n", resp);
    }
}