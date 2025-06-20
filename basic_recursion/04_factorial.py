'''

Problem Statement: Given a number X,  print its factorial.

Examples:

Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1

Example 2:
Input: X = 3
Output: 6
Explanation: 3!=3*2*1

'''


def factorial(n):

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))