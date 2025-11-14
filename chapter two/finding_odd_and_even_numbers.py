#Exercise 2.6 this program collects user inputs and dertermines the if the input is odd or even

number_one = int(input('Hey There, enter a number and we will determine if its an even or odd number: '))

if number_one % 2 == 0:
       print(number_one, 'is an even number\n')

else:
       print (number_two, 'is an even number')

number_two = int(input('Enter another number: '))
if number_two % 2 == 0:
    print(number_two, 'is an even number')

else:
    print(number_two, 'is an odd number')

