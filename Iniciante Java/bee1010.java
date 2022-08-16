// 1010 - Cálculo Simples
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int c1, n1, c2,n2;
        double vlr1, vlr2, total;
        Scanner sc = new Scanner(System.in);
        c1 = sc.nextInt();
        n1 = sc.nextInt();
        vlr1 = sc.nextDouble();
        
        c2 = sc.nextInt();
        n2 = sc.nextInt();
        vlr2 = sc.nextDouble();
        
        total = (vlr1 * n1) + (vlr2 * n2);
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", total);
    }
}