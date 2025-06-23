'''

Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)


Solution Approach: Using recursion.

 the first number is 0, and second number is 1, similarly we can get the third number by adding the previous 2 digits as: f(3) = f(2) + f(1), so, f(n) = f(n-2) + f(n-1)

'''

N = 7

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(N + 1):
    print(fib(i), end = " ")