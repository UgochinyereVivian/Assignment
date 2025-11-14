
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
