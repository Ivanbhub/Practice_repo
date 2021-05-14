"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
"""

import random 
import string

pw = []

for i in range(10): # A 10 Characters password 
    upper_case = random.choice(string.ascii_letters[26:-1]) 
    lower_case = random.choice(string.ascii_letters[0:26])
    number= random.choice(string.digits)
    special_char= random.choice(string.punctuation)
    # to avoid predictability, I randomized how characters follow each other;  
    pw_generator=[upper_case,lower_case,str(number),special_char]
    # Append the random characters one by one 
    pw.append(random.choice(pw_generator))
    
random_password = ''.join(pw)

print(random_password)




#                      """ Short Version"""
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)
