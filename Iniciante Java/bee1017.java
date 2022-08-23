// 1017 - Gasto de Combustível
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int tG,vM;
        double km,qL;
        Scanner sc = new Scanner(System.in);
        tG = sc.nextInt();
        vM = sc.nextInt();
        km = tG * vM;
        qL = km/12;
        System.out.printf("%.3f\n", qL);
    }
}