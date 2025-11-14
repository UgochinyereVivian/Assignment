import java.util.Scanner;
    public class LeapYear{
public static void main(String[]arags){

Scanner input = new Scanner(System.in);

System.out.println("enter the number of days in a year\n");
int days = nextInt();

if (days % 4 == 0 &&  days % 100){
        System.out.println("This a leap year");
}else {
        System.out.println("this is not leap year");   
} 

 }
