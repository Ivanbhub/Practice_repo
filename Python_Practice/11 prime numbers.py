"""Ask the user for a number and determine whether the number 
is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below."""

number = int(input('Type your number here --> '))

def  Prime_number (num):
    divisors = [2, 3, 5, 7, 11]
    for i in divisors:
        if num % i==0:
            print('your number is not a prime number'  )
            break
        else:
            print('your number is a prime number')
            break
    
        
        
Prime_number (number)


# didn't use my answer to Exercise 4
