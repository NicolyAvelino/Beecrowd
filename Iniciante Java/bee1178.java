// 1178 - Preenchimento de Vetor III
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double x = sc.nextDouble();
        for(int i=0; i<100; i++){
            if(i == 0){
                System.out.printf("N[%d] = %.4f\n",i,x);
            } else{
                System.out.printf("N[%d] = %.4f\n",i,x/2);
                x = x / 2;
            }
        }
    }
}