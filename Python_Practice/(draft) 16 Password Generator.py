"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""


import random 
import string

letters = (string.ascii_letters)
pw = []
special_character=['@','#','$','%','&','!']

for i in range(10):
    upper_case = random.choice(letters[26:-1])
    lower_case = random.choice(letters[0:26])
    number= random.randint(0,10)
    special_char= random.choice(special_character)
    pw_generator=[upper_case,lower_case,str(number),special_char]
    pw.append(random.choice(pw_generator))

    
    
random_password = ''.join(pw)

print(random_password)
