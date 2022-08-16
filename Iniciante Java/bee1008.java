// 1008 - Salário
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int nF,nHT;
        double vH, total;
        Scanner sc = new Scanner(System.in);
        nF = sc.nextInt();
        nHT = sc.nextInt();
        vH = sc.nextDouble();
        total = nHT * vH;
        System.out.printf("NUMBER = %d\n", nF);
        System.out.printf("SALARY = U$ %.2f\n", total);
    }
}