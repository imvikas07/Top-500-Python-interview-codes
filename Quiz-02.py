'''
Check Whether a Number is Even or Odd in Python
Given an integer input the objective is to write a Python code to Check Whether a Number is Even or Odd. To do so the main idea is to divide the number by 2 and check if it’s divisible or not. It’s an Even number is it’s perfectly divisible by 2 or an Odd number otherwise.

Here are the Methods to solve the above mentioned problem,

Method 1 : Using Brute Force
Method 2 : Using Ternary Operator
Method 3 : Using Bitwise Operators


'''


# Method 1 : Using Brute Force

usrInput = int(input('Enter your Number: '))

if usrInput % 2 ==0:
    print('Number is even')
else:
    print('number is odd')


# Using Ternary Operator

usrNumber = 5

print('even' if usrNumber %2 ==0 else 'odd')


#Method 3 : Using Bitwise Operators

def isEven(num):
    return num &1

if __name__ == "__main__":
    num = 13
    if isEven(num):
        print('even')
    else:
        print('odd')


