#Exercise 2.10 this program collects inputs three integers from the user. Display the sum, average, product, smallest and largest of the number

integer_one = int(input('Hey There, Enter a whole number: '))
integer_two = int(input('Hey There, Enter a second whole number: '))
integer_three = int(input('Hey There, Enter a third whole number: '))

sum = integer_one + integer_two + integer_three
product = integer_one * integer_two * integer_three
average = (integer_one + integer_two + integer_three) // 3

smallest = integer_one
largest = integer_one

if integer_two < smallest: 
    print(integer_two, 'is the smallest')

elif integer_three < smallest:
    print(integer_two, 'is the smallest') 

else:
    print('the smallest is', smallest)

if integer_two > largest: 
    print(integer_two, 'is the laragest')

elif integer_three > largest:
    print(integer_three, 'is the largest')

else: 
    print('the largest is', largest)

