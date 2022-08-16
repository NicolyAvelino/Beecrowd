// 1006 - Média 2
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double n1,n2,n3,media;
        Scanner sc = new Scanner(System.in);
        n1 = sc.nextDouble();
        n2 = sc.nextDouble();
        n3 = sc.nextDouble();
        media = (n1*2 + n2 * 3 + n3 * 5)/10;
        System.out.printf("MEDIA = %.1f\n", media);
    }
}