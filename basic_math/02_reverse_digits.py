'''
Problem Statement: Given an integer N return the reverse of the given number.

Important Notes: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

Example 1:
        Input:N = 12345

        Output:54321

Example 2:
        Input:N = 10
        Output:1

Solution Approach:

Brute Force: take out the last digit using modulo and divide the given integer by 10 and multiply the stored reversed digit by 10 with the addition to remainder obtained
Optimal :

'''

number = 12345

def reverse_digits(num):
    reversed_num = 0
    while num > 0:
        rem = num % 10
        reversed_num = reversed_num * 10 + rem
        num = num // 10

    return reversed_num

print(reverse_digits(number))