# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)



rock=1
paper=2
scissors=3

player2=0
player1=0

while player1 not in[1,2,3]:
    player1 = int(input('''First player, choose one number:1:rock 2: paper 3:scissors --> '''))

while player2 not in[1,2,3]:
    player2 = int(input('''second player, choose one number:1:rock 2: paper 3:scissors--> '''))
    continue

if player1==player2:
    print('it is a tie')
    
if player1==1 and player2 ==2:
    print('Player2 WINS!!!!!')
