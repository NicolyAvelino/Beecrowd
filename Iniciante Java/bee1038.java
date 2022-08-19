// 1038 - Lanche

import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		// declaração de variável
		int cd, qt;
        double pg, preco;
        
		// cria um objeto scanner
		Scanner sc = new Scanner(System.in);
 
		// receber o codigo do usuario
		cd = sc.nextInt();
		qt = sc.nextInt();

		// calculando usando if
        if(cd == 1){
            preco = 4.00;
        } else if(cd == 2){
            preco = 4.50;
        } else if(cd == 3){
            preco = 5.00;
        } else if(cd == 4){
            preco = 2.00;
        } else {
            preco = 1.50;
        }
        
        // calculando
        pg = preco * qt;
        
        // saida de dados
        System.out.printf("Total: R$ %.2f\n",pg);
	}
}

