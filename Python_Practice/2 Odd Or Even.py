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
    print('Ooopss, {} cannot divide {} evenly, Try again later!'.format(Check, Num))
