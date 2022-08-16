// 1011 - Esfera
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double r, vol;
        Scanner sc = new Scanner(System.in);
        r = sc.nextDouble();
        vol = (4/3.0) * 3.14159 * (r*r*r);
        System.out.printf("VOLUME = %.3f\n", vol);
    }
}