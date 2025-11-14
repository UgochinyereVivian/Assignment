
// java version of grading_using_average.py

import java.util.Scanner;
    public class GradingUsingAverage{
public static void main(String[]arags){

Scanner input = new Scanner(System.in);

System.out.println("Enter the score for course one (english): ");
int scoreOne = input.nextInt();

System.out.println("Enter the score for course two: ");
int scoreTwo = input.nextInt();


System.out.println("Enter the score for course three: ");
int scoreThree = input.nextInt();

int average = (scoreOne + scoreTwo + scoreThree) / 3;

if (90 <= average  && average <= 100)
    System.out.println('A');

else if (80 <= average && average < 90)
     System.out.println('B');

else if (70 <= average && average < 80)
     System.out.println('C');
else if (60 <= average && average < 70)
     System.out.println('D');
else
     System.out.println('F');

}
 }
