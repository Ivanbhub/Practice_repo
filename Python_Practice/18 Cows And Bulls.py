"""Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

"""

import random 

random_number= str(random.randint(1000,9999))
print(random_number)

#print(random_number[0:1])

def user_guess():
    number_guessed = str(input('guess a 4 digits number --> '))
    print(number_guessed[0])
    
user_guess()
