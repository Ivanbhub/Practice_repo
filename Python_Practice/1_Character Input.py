# LINK to the exercice: http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import datetime
currentYear= datetime.now().year #  gets the current year that will be used later on
name = input('what\'s your name: ')

age = int(input('How old are you? : '))

Year100= currentYear+(100 - age) # adds the dif to currrent year

print('Hey {}, you will turn 100 in {} '.format(name, Year100))

number=int(input('How many times do you want to see the previous message?-->'))
i = 0 
while i != number :
    print('Hey {}, you will turn 100 in {} '.format(name, Year100))
    i=i+1
