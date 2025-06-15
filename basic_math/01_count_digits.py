
'''
Problem Statement: Given an integer N, return the number of digits in N.

Example 1:
        Input:N = 12345

        Output:5

Solution Approach:

Brute Force: divide the number by 10 and count how many times the division can be done.
Optimal : use math module as count = int(math.log10(n) + 1)
'''

import math

def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count

print(count_digits(10))