"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""


def fib_function(a):
    a = int(input('How many fib numbers? -->  '))
    i=0
    fib = 1
    for i in range(1,a):
        
        fib= fib+fib
        print(fib)
        #print(i)
        i=i+1

fib_function(5)
