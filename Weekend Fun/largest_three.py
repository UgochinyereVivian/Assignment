a = int(input('Hey Odili,enter a whole number: '))
b = int(input('Enter another whole number: '))
c = int(input ('Enter another whole number: '))

largest = a

if b > a and b > c:
    print('the largest number is: ', b)
if c > a and c > b:
    print('the largest number is: ', c)
else: 
    print ('the largest number is: ', largest)


