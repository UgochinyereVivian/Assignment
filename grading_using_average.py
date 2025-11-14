score_one = int(input("Enter course score that is less or equal to 90 and less than 100: ")) 
score_two = int(input("Enter the score for course two (english): "))
score_three = int(input("Enter the score for course three: "))

average = (score_one + score_two + score_three) // 3

print ('the average score is', average, '\t')

print("Letter Grade")


if 90 <= average   and average <= 100:
    print('A')

elif 80 <= average and average < 90:
    print(B)

elif 70 <= average and average < 80:
    print(C)
elif 60 <= average and average < 70:
    print('D')
else:
    print('F')
