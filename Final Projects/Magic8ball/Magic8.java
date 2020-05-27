import java.util.Random;
import java.util.Scanner;

public class Magic8 {


    public static void main(String[] args) {
        System.out.println("What do you wish to ask?");
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println("You have asked \""+str+"\"");

        Random rand = new Random();
        int rnum = rand.nextInt(8);
        
        switch (rnum){
            
            case 0:
                System.out.println("Does not seem likely");
                break;
            case 1:
                System.out.println("Don't bet on it");
                break;
            case 2:
                System.out.println("Ask again later");
                break;
            case 3:
                System.out.println("The spirits refuse to answer");
                break;
            case 4:
                System.out.println("Possibly");
                break;
            case 5:
                System.out.println("Maybe");
                break;
            case 6:
                System.out.println("Most probably");
                break;
            case 7:
                System.out.println("It is certain");
                break;
            case 8:
                System.out.println("I have no clue");
                break;
            default:
                System.out.println("Ya dun broke'd it");
                break;
            

        }
    }
}