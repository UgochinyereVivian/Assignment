

// java version of password_strength_checker.py

import java.util.Scanner;
    public class PasswordStrengthChecker{
public static void main(String[]arags){

Scanner input = new Scanner(System.in);

System.out.println("Hello 👋️ welcome to my app, follow he instructions below to log in \n");

System.out.println("Enter your login password:");
String password = input.nextLine();

if (password.length() > 6 && password.length() <= 10)
     System.out.println("medium");

else if (password.length() < 6)
     System.out.println("weak");

else if (password.length() > 10)
     System.out.println("strong");

else if (password.length() < 1)
     System.out.println("invalid");

}
 }


