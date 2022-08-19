import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int x;
        double y, cons;

        Scanner sc = new Scanner(System.in);

        x = sc.nextInt();
        y = sc.nextDouble();

        cons = x / y;

        System.out.printf("%.3f km/l\n", cons);
    }
}