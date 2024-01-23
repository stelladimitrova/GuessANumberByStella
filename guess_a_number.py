import random

name = input('Enter your name:')

print(f'Hello, {name}! You are about to play a game called Guess A Number.\nThink of a number between 1-100 and see if'
      f' you guessed it right.')

computer_number = random.randint(1, 100)

while True:
    player_input = input('Write your guess here (1-100):')

    if not player_input.isdigit():
        print('Invalid Input! Try again...')
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print('Success! You guessed it!')
        break

    elif player_number > computer_number:
        print('Too High!')

    else:
        print('Too Low!')

