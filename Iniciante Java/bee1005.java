// 1005 - Média 1
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double n1,n2,media;
        Scanner sc = new Scanner(System.in);
        n1 = sc.nextDouble();
        n2 = sc.nextDouble();
        media = (n1*3.5 + n2 * 7.5)/11;
        System.out.printf("MEDIA = %.5f\n", media);
    }
}