"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me."""

def reverse_words():
    user_input= input('Enter a sentence? --> ')
    List_with_split_words = user_input.split() 
    List_with_split_words.reverse()
    Reversed_Sentence = ' '.join(List_with_split_words)
    print(Reversed_Sentence)
    
reverse_words()
