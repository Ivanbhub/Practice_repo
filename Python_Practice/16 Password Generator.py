"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
"""


import random 
import string
import time

letters = (string.ascii_letters)
pw = []
special_character=['@','#','$','%','&','!']

for i in range(10): # A 10 Characters password 
    upper_case = random.choice(letters[26:-1]) 
    lower_case = random.choice(letters[0:26])
    number= random.randint(0,9)
    special_char= random.choice(special_character)
    # to avoid predictability, I randomized how characters follow each other;  
    pw_generator=[upper_case,lower_case,str(number),special_char]
    # Append the random characters one by one 
    pw.append(random.choice(pw_generator))
    
random_password = ''.join(pw)

print(random_password)

print(f'your program run-time was {runTime} seconds')



                      """ Short Version"""
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)

