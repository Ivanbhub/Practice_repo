'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''
import random

def no_duplicates(Length_of_list):
    random_list = []
    for i in range(0,Length_of_list):
        x = random.randint(0,10)
        random_list.append(x)
    print(f'The following is the list w/o duplicate filter: {random_list}')
    print(f'Here is how it looks after applying the filter: {set(random_list)}')

no_duplicates(10)
