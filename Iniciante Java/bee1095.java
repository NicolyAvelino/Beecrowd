// 1095 - Sequencia IJ 1
public class Main {
    public static void main(String[] args) {
        int con,i,j;
        con = 0;
        i = 1;
        j = 60;
        while(con <= j){
            System.out.printf("I=%d J=%d\n",i,j);
            i += 3;
            j -= 5;
        }        
    }
}