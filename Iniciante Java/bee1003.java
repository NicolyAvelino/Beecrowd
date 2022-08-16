// 1003 - Soma Simples
import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        int n1,n2,soma;
        Scanner sc = new Scanner(System.in);
        n1 = sc.nextInt();
        n2 = sc.nextInt();
        soma = n1 + n2;
        System.out.printf("SOMA = %d\n", soma);
    }
}