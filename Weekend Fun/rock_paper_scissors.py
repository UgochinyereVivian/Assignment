print('Hey Peeps!🤩️🤸‍♀️️ITS FUN TIME!!!!🤽️🤼‍♂️️\n')

print('LETS PLAY THE ROCK, PAPER, SCIISORS GAME🤸‍♀️️\n YOU vs CHOPZIEEEE🤡️!!!! \n NOW FOLLOW THE GAMING RULES AND MAKE AN INPUT TO KNOW WHO WINS!\n')


first_user_letter = input('Enter any of the following; Rock, Paper, Scissors: \n')
second_player_letter = input('Enter any of the following; Rock, Paper, Scissors: \n')

if first_user_letter == ("Rock" and second_player_letter == "scissors") or (first_user_letter == "paper" and second_player_letter == "rock") or (first_user_letter == "scissors" and second_player_letter == "paper") :
    print('player 1 wins')


elif second_player_letter == ("Rock" and first_user_letter == "scissors") or (second_player_letter == "paper" and first_user_letter == "rock") or (second_player_letter == "scissors" and first_user_letter == "paper") :
    print('player 2 wins')


elif second_player_letter == "Rock" and first_user_letter == "Rock" or  second_player_letter == "paper" and first_user_letter == "paper":
    print('both player wins') 



