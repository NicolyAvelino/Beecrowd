// 1012 - Área
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double A,B,C, t,c,tp,q,r;
        Scanner sc = new Scanner(System.in);
        A = sc.nextDouble();
        B = sc.nextDouble();
        C = sc.nextDouble();
        
        t = (A * C) / 2;
        c = 3.14159 * (C * C);
        tp = ((A + B) * C)/2;
        q = B * B;
        r = A * B;
        
        System.out.printf("TRIANGULO: %.3f\n", t);
        System.out.printf("CIRCULO: %.3f\n", c);
        System.out.printf("TRAPEZIO: %.3f\n", tp);
        System.out.printf("QUADRADO: %.3f\n", q);
        System.out.printf("RETANGULO: %.3f\n", r);
    }
}