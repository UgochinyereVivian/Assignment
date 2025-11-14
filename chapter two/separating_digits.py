#Exercise 2.11 this code separates digits in an integer

integer_one = int(input('Hey There, Enter a five digits whole number: '))

number_one = integer_one // 10000 % 10
number_two = integer_one // 1000 % 10
number_three = integer_one // 100 % 10
number_four = integer_one // 10 % 10
number_five = integer_one % 10
print(f"{number_one} \t {number_two} \t {number_three} \t {number_four} \t {number_five}")

