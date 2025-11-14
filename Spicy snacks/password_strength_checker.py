#        PSEUDOCODE
#1. I go first welcome my correct customer wey subcribe to my Ai powered app
#2. I go come create container wey go collect password to access the app. 
#3. I go come put inside the cointainer anything wey my loyal customer type as en password
#4. I go come check the number of wetin my customer enter
#5  I go write say if the length of wetin en write is GREATER than six but less than or equal to 10
#6  If 15 above dey true, i go tell my user by display say the password strength "medium"
#7. I go write again to see if length pass 10
#8  If true true the length pass 10, i go tell my user say the password strength dey 'Strong'
#9  In case no 6 and 8 no true, i go write to check if password is less than 6
#10.If no 9 is true, i will tell my user say na "weak" password
#11. If that one fail, unto say en password no reach, i go write to check if the password is less than one
#12. if its less than one, i go tell my user "invalid" password

print ("Hello 👋️ 1welcome to my app, follow he instructions belo to log in \n")
 
password = input("Enter your login password:") 


if len(password) > 6 and len(password) <= 10:
    print('medium')

elif len(password) < 6:
    print('weak')

elif len(password) > 10:
    print('Strong')

elif len(password) < 1:
    print('invalid')
