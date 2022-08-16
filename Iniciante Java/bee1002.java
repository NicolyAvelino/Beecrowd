// 1002 - Área do Círculo
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double n,raio,area;
        n = 3.14159;
        Scanner sc = new Scanner(System.in);
        raio = sc.nextDouble();
        area = n * (raio * raio);
        System.out.printf("A=%.4f\n", area);
    }
}