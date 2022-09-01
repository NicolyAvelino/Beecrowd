// 3342 - Keanu
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n%2==0){
            int div = (n*n)/2;
            System.out.printf("%d casas brancas e %d casas pretas\n",div,div);
        } else{
            int div = (n*n)/2;
            System.out.printf("%d casas brancas e %d casas pretas\n",div+1,div);
        }
    }
}