# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
word = str(input('What word are we checking today? --> '))

word_split=[]
#word_reverse=[]

for i in word :
    word_split.append(i)
    
print(word_split)

word_split.reverse()
print(word_split)

if word_split == word:
    print('it\'s a palindrome' )
    
else:
    print('Try again')
