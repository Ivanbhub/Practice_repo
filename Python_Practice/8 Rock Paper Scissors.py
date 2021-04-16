# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

# This code can be shorter, but for practice purposes I wrote more line of code

rock=1
paper=2
scissors=3

player2=0
player1=0

new_game='yes'

while new_game=='yes':
    
    while player1 not in[1,2,3]:
        player1 = int(input('''First player, choose one number:1:rock 2: paper 3:scissors --> '''))

    while player2 not in[1,2,3]:
        player2 = int(input('''second player, choose one number:1:rock 2: paper 3:scissors--> '''))
        continue
    
    if player1==player2:
        print('it is a tie')
     # ROCK   
    if player1==1 and player2 ==2:
        print('Player2 WINS!!!!!')
    if player1==1 and player2 ==3:
        print('Player1 WINS!!!!!')
        
    # Paper 
    if player1==2 and player2 ==1:
        print('Player1 WINS!!!!!')
    if player1==2 and player2 ==3:
        print('Player2 WINS!!!!!')
        
    # scissors
        
    if player1==3 and player2 ==1:
        print('Player2 WINS!!!!!')
    if player1==3 and player2 ==2:
        print('Player1 WINS!!!!!')
        
    new_game= input('do you want to start a new game? type yes or no : ' )
    player2=0
    player1=0
    
