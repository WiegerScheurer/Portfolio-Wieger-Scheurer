/*
 * Naam        : W. Scheurer
 * UvAnetID    : 11349433
 * Studie      : BSc Informatica
 * Deel4.java  : Dit programma vraagt de gebruiker om een positief geheel getal te geven als input, welke vervolgens getransformeerd wordt in datzelfde
 *               aantal elementen van de Lucas-reeks vanaf de start van de reeks. Er is een vaste range aan getallen die volstaat, te grote getallen 
 *               worden weggefilterd. 
 */
import java.util.Scanner;
import java.util.Arrays;
import java.lang.reflect.Array;
public class Deel4 {
    public static void main(String [] args) {
        System.out.print("Geef een natuurlijk getal: ");
        /*
         * Registratie van input door gebruiker aan de hand van de Scanner class.
         */
        Scanner scanner = new Scanner (System.in);
        int input   = 0;
        input       = scanner.nextInt();
        /*
         * Exclusie van invalide input. Zowel '0' als negatieve waarden als input resulteren in het beeindigen van het programma na selectie
         * middels een 'if' statement.
         */    
        if (input < 0)
            {
                System.out.println("Dit is een negatief getal, ik sluit af.");
                System.exit(1);
            }
            if (input == 0)
            {
                System.out.println("Dit is niet genoeg om een reeks te vormen, ik sluit af.");
                System.exit(1);
            }
            /*
             * Creatie van de array waar later de Lucas-reeks in gezet zal worden.
             */    
            int[] lucas = new int[input]; 
                    lucas[0]    = 2;
                    int element = 0;
                    /*
                    * Aparte output voor wanneer de input 1 is, zodat de zin kloppend is.
                    */
                    if (input == 1)
                    {
                        System.out.println("Het eerste Lucas-getal is: " + lucas[0]);
                        System.exit(1);
                    }
                    /*
                     * Berekening van Lucas-getallen door middel van een formule verwerkt in een for-loop. Exclusie van waarden die een te groot getal
                     * opleveren om als integer verwerkt te worden vindt plaats door middel van een 'if' statement binnen de for-loop.
                     */
                    else
                    {
                        lucas[1]    = 1;
                        for (element = 0; element < input -2; element++)
                        {
                            lucas[element +2] = lucas[element] + lucas[element +1];
                            if (lucas[(element +2)] <= 0)
                            {
                                System.out.println("Dit getal is te groot, het past niet.");
                                System.exit(1);
                            }
                        }
                    /*
                     * Uiteindelijke output met enkele aanpassingen qua interpunctie zodat het overeenkomt met de opgave.
                     */
                        System.out.println("De eerste " + input + " Lucas-getallen zijn: " + Arrays.toString(lucas).replace("[", "").replace("]", "").replace(",", "")); 
                    }

    }
}