

print("Hello🤩️you will enter two numbers and arithmetic operators and the result will be printed for you!")

number = int(input("Enter your first number: ")) 

numbertwo = int(input("Enter Second number: "))

operator = input("now, enter an operator (+,-, * etc):")

if operator == "+" :
    print(number + numbertwo )

elif operator == "*" :
    print(number * numbertwo )

elif operator == "**" :
    print(number ** numbertwo )

elif operator == "/" :
    print(number / numbertwo )

elif operator == "//" :
    print(number // numbertwo )

elif operator == "-" :
    print(number - numbertwo )


#result = number, operator, numbertwo
#
#print(result)
