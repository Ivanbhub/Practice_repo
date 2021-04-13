# Link to the practice problem : http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html


Number = int(input('What\'s your number? --> '))

if Number % 2 == 0 :
    print('Your number is EVEN')
else:
    print('That\'s and ODD number')
    


if Number % 4 == 0 :
    print('Your number is also a multiple of four')
    
    
print('\n')
Num = int(input('What number are you dividing? --> '))

Check = int(input(' Divide by ? --> '))

if Num % Check == 0 : 
    print('Congratulations!!,{} divide {} evenly'.format(Check, Num))
    
else:
    print('Ooopss, {} cannot divide {} evenly, try again later!'.format(Check, Num))
