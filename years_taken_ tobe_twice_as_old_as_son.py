#        PSEUDOCODE
#1. 1. I first create a storage container that will hold the father’s age/input.
#2. I then create another container that will store the son’s age
#3. I will ask the father to enter his age, and whatever he inputs is placed into the father-age container.
#4. I ask the son to enter his age, and whatever he inputs is placed into the son-age container.
#5. I create a math storage to house the maths i will carry out 
#6. perform the mathematics of multiplying whatever is the sons input by 2 
#7. I will perform another maths taht substracting the sons input from the fathers input
#7. I willl then place in that math storage the result of the calculation
#8. I will print and display the result of the maths performed as the solution to the question.


fathers_age = int(input('Hey There Dad, Enter your age (stay within the range of 1 -80: '))
sons_age = int(input('Hey There Son, Enter your age (stay within the range of 1 -80: '))

result = fathers_age - 2 * sons_age
print('it will take', result, ' years to be twice as old')




