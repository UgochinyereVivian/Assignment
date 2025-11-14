
// java version of father_years_taken_ tobe_twice_as_old_as_son.py

import java.util.Scanner;
    public class AgeIfFathersAgeIsTimesTwoOfSonsAge{
public static void main(String[]arags){

Scanner input = new Scanner(System.in);

System.out.println("'Hey There Dad, Enter your age (stay within the range of 1 -80:");
int fatherAge = input.nextInt();

System.out.println("'Hey There Son, Enter your age (stay within the range of 1 -80:");
int sonAge = input.nextInt();

int result = fatherAge - (2 * sonAge);

System.out.println("result");

}
 }
