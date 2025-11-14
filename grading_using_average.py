#        PSEUDOCODE
#1. I go first secure correct container wey go holl score a student get for one particular course
#2. I go run another container to store another course score for that same student
#3. I go ask that student make en give me wetin en get for course one.
#4. I go still ask am fior wetin en get for course two
#5  I go ensure say i write input place am for that first container wey i keep.
#6  I go ensure say wetin en go write for course two go enter the second container sharp sharp
#7. I go come bring another container wey go house the maths wey i go run
#8  Inside that maths container i go add everything wey that student put as en score
#9  After i add am finish i go divide by how many scores wey en enter, if na two score na by two
#10.I go come print say if that score big pass 90 or na 90 gon gon but less or equal 100  make them knack that student A
#11. If that one fail, unto say en score no reach, i go come print say if that score big pass 80 or na 80 sharp but less tha 90  make them knack that student B
#12. If that one fail, i go come print say if that score big pass 70 or na 70 gon gon but less than 80  make them knack that student C, e try
#13. If that one fail, i go come print say if that score big pass 60 or na 60 gon gon but less than 70 make them knack that student D, e don esacape.
#14 If that one still fail, i go come print say knack am "F", NA OLODO be that, collect en school fees back.


score_two = int(input("Enter the score for course two (english): "))
score_three = int(input("Enter the score for course three: "))

average = (score_one + score_two + score_three) // 3

print ('the average score is', average, '\t')

print("Letter Grade")


if 90 <= average   and average <= 100:
    print('A')

elif 80 <= average and average < 90:
    print('B')

elif 70 <= average and average < 80:
    print('C')
elif 60 <= average and average < 70:
    print('D')
else:
    print('F')
