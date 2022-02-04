import java.util.Scanner;

public class palindrome
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter sentence to check for the palidrome.");
        String Line = sc.nextLine();
        Line = Line.toLowerCase();
        Line = Line.replaceAll("[/.<>?';]", "");
        Line = Line.replaceAll(" ", "");
        String Rev = "";

        int length = Line.length();
        for (int i = length-1; i >= 0; i--)
        {
            Rev = Rev + Line.charAt(i);
        }
        if (Line.equals(Rev))
        {
            System.out.println("Sentence/Word is palindrome.");
        }
        else
        {
            System.out.println("Sentence/Word is not palindrome");
        }
    }
}
