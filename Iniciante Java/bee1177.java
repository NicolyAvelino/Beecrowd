// 1177 - Preenchimento de Vetor II
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int vet[] = new int[1000];
        
        for (int i = 0; i<1000; i++){
            vet[i]=i % T;
            System.out.printf("N[%d] = %d\n", i, vet[i]);
        }
    }
}