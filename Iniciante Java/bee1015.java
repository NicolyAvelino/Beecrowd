// 1015 - Distância Entre Dois Pontos
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double x1,y1;
        double x2,y2;
        Scanner sc = new Scanner(System.in);
        x1 = sc.nextDouble();
        y1 = sc.nextDouble();
        x2 = sc.nextDouble();
        y2 = sc.nextDouble();
        double dist = Math.sqrt(Math.pow(x2 - x1,2) + Math.pow(y2 - y1,2));
        System.out.printf("%.4f\n", dist);
    }
}