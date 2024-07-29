'''
Find the Sum of the First N Natural Numbers in Python
Given an integer input of N, the objective is to find the sum of all the natural numbers until the given input integer. To do so we can use different approaches to write the Python code and some such methods are mentioned below,

Method 1 : Using for Loop
Method 2 : Using Formula for the Sum of Nth Term
Method 3 : Using Recursion

'''

# Method 1: Using for loop

num = int(input('Enter Number: '))
sum = 0
for i in range(num+1):
    sum+=i
print(sum)


# Method 2 : Using Formula for the Sum of Nth Term

'''
Formula to Find the Sum of N terms
Sum = ( Num * ( Num + 1 ) ) / 2
'''

num = 5

print(int(sum *(sum +1))/2)


# Method 3 : Using Recursion

def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 5
print(getSum(num))



