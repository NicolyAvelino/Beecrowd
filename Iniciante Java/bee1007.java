// 1007 - Diferença
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int A,B,C,D,dif;
        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();
        dif = (A * B - C * D);
        System.out.printf("DIFERENCA = %d\n", dif);
    }
}