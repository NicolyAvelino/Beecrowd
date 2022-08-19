// 1042 - Sort Simples

import java.util.Scanner;
import java.util.Arrays;
public class Main {
	public static void main(String[] args) {
		// declaração de variáveis
		int n1,n2, n3;

		// cria um objeto scanner
		Scanner sc = new Scanner(System.in);

		// receber valor 1 do usuario        
		n1 = sc.nextInt();
        n2 = sc.nextInt();
        n3 = sc.nextInt();

        // realizando operação, colocando os valores em um vetor e usando sort para ordenar
		int[] num = {n1,n2,n3};
		Arrays.sort(num);

		// saida de dados
        for(int i=0; i < 3; i++){
            System.out.printf("%d\n",num[i]);
        }
        System.out.println();
        System.out.printf("%d\n",n1);
        System.out.printf("%d\n",n2);
        System.out.printf("%d\n",n3);

		//System.out.printf(Arrays.toString(num));	    
	}
}