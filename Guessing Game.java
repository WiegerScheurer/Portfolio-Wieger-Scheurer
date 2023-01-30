/*
 * Naam        : W. Scheurer
 * UvAnetID    : 11349433
 * Studie      : BSc Informatica
 * Deel3.java  : In dit programma wordt er een kansspel uitgevoerd waarin de gebruiker 3 kansen krijgt een willekeurig gegenereerd getal 
 *               tussen de 1 en 10 te raden. Wanneer er een getal buiten de genoemde range als input gegeven wordt, stopt het programma vroegtijdig.
 */
import java.util.Random;
import java.util.Scanner;
public class Deel3 {
    public static void main(String [] args) {
        /* 
         * Creatie van een willekeurig getal tussen 1 en 10.
         */
        Random rand = new Random();
        int getal = rand.nextInt(10) + 1;
        /*
         * Print van vraag richting gebruiker en registratie input door middel van de scanner class.
         */
        System.out.println("Geef een getal tussen de 1 en 10, je mag drie keer raden");
        int pogingen = 1;
        /*
         * De geslaagd integer wordt gebruikt als switch voor wanneer het goede getal is geraden.
         */
        int geslaagd = 0;
        for (pogingen = 1; pogingen < 4; pogingen++)
        {
            Scanner scanner = new Scanner (System.in);
                int input = 0;
                input       = scanner.nextInt();
                    if (pogingen == 1)
                    {
                        System.out.println("eerste keer: " + input);
                    }
                    if (pogingen == 2)
                    {
                        System.out.println("tweede keer: " + input);
                    }
                    if (pogingen == 3)
                    {
                        System.out.println("derde keer: " + input);
                    }
                    /*
                    * Controle of de gegeven input tussen de 1 en 10 valt door 'if' statement te gebruiken.
                    */
                    if (input <= 0 || input > 10)
                    {
                        System.out.println("Getal was niet tussen 1 en 10, dan stop ik");
                        System.exit(1);
                    }
                    /*
                     * Gebruik 'if' statement om te checken of de input groter/kleiner is dan het willekeurig gegenereerde getal, of dat deze gelijk 
                     * is aan het willekeurig gegenereerde getal.
                     */
                    if (input < getal)
                    {
                        System.out.println("te klein");
                    }
                    if (input > getal)
                    {
                        System.out.println("te groot");
                    }
                    if (input == getal)
                    {
                        geslaagd = 1;
                        System.out.println("gewonnen");
                        System.exit(1);
                    }
                    /*
                     * Door een 'if' statement te combineren met het aantal pogingen en de geslaagd integer die op '0' blijft staan wanneer er 
                     * enkel foute input gegeven wordt, print het systeem een teleurstellend bericht.
                     */
                    if (pogingen == 3 & geslaagd == 0)
                    {
                        System.out.println("verloren, het getal was " + getal);
                    }
        }
    }
}



