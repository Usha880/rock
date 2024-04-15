import random

def game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input('Welcome to Rock, Paper, Scissors!\n\nPlease choose rock, paper, or scissors: ')
    while user_choice not in choices:
        print('Invalid input, please try again.')
        user_choice = input('Please choose rock, paper, or scissors: ')

    print('Computer chose: ', computer_choice)

    if user_choice == computer_choice:
        return 'It\'s a tie!'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

print(game())

play_again = input('Do you want to play again? (yes/no): ')
while play_again == 'yes':
    print(game())
    play_again = input('Do you want to play again? (yes/no): ')