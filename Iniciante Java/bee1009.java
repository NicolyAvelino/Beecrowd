// 1009 - Salário com Bônus
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        String nm;
        double slr,vendas,total;
        Scanner sc = new Scanner(System.in);
        nm = sc.next();
        slr = sc.nextDouble();
        vendas = sc.nextDouble();
        
        total = slr + (vendas * 0.15);
        System.out.printf("TOTAL = R$ %.2f\n", total);
    }
}