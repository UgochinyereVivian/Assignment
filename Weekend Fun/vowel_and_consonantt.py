letter = input('Hey Odili, enter one letter: ')

if letter.isdigit():
    print('invalid input')

if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o' ) or (letter == 'u'):
    print("Vowel")

if (letter != 'a') or (letter != 'e') or (letter != 'i') or (letter != 'o' ) or (letter != 'u'):
    print("CONSONANT")




#OR I CAN USE 'IN'


#letter = input('Hey Odili, enter one letter: ')
#letter_one = "aeiou"
#letter_two = "bcsfghjklmnpqrstvwxyz"
#
#if letter in letter_one:
#    print("vowel")
#
#elif letter in letter_two:
#    print("consonant")
#
#elif letter.isdigit():
#    print('invalid input')
  


