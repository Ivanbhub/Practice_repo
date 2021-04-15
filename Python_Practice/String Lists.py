# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)



word = str(input('What word are we checking today? --> '))

word_split=[]

# I SPLIT thhe word add it to the list, REVERSE it, JOIN it and check if it reads the same
for i in word :
    word_split.append(i)

word_split.reverse()

check_word = ''.join(word_split)
print("your word reversed is '{}'".format(check_word))

if check_word == word:
    print('it\'s a palindrome!!' )
    
else:
    print('Sorry, your word is not a palindrome, try again')
