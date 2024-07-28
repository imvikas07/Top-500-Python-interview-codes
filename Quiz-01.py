# Python Program to check if a Number Is Positive Or Negative

'''
Check if a Number is Positive and Negative in Python
Given an integer input, the objective is check whether the given integer is Positive or Negative. In order to do so we have the following methods,

Method 1: Using Brute Force
Method 2: Using Nested if-else Statements
Method 3: Using ternary operator

'''

# Method 1: Using the Brute Force

num = int(input('check number: ')) #Assign number to check condition

if num > 0:
    print('positive number')
elif num < 0:
    print('negtive')
else:
    print('zero')


#Method 2: Using Nested if-else Statements

num = 15 

if num >= 0:
    if num == 0:
        print('zero')
    else:
        print('postive')
else:
    print('negtive')
    
#Method 3: Using ternary operator

num = 15

print('positive' if num >=0 else 'negitive')

