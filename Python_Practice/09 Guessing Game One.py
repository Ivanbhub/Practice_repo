#http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (_Hint: remember to use the user input lessons from the very first exercise

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''




import random 


Number_to_guess= random.randint(1,9)

User_guess = 0

tries = 0


while True:
    User_guess= input('''Enter a number between 1 and 9 (type 'exit' to quit) --> ''')
    

    if User_guess == 'exit':
        print('Thanks for trying')
        break
    User_guess = int(User_guess)
    if User_guess > Number_to_guess:
        print(' Too high ')
    if User_guess < Number_to_guess:
        print(' Too low ')
        
    if User_guess == Number_to_guess:
        print(' You guessed the number right')
        break
    tries = tries+1
    
    
print('Thanks for playing the game, you used {} lives'.format(tries))
        
    
