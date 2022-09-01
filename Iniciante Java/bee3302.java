// 3302 - Resposta Certa
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for(int i=1; i <=N; i++){
            int num = sc.nextInt();
            System.out.printf("resposta %d: %d\n",i,num);
        }
    }
}