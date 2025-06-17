'''

Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

The Greatest Common Divisor of any two integers is the largest number that divides both integers.

Example 1:

Input:N1 = 9, N2 = 12
Output:3

Explanation:Factors of 9: 1, 3 and 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

Example 2:
Input:N1 = 20, N2 = 15
Output: 5
Explanation:Factors of 20: 1, 2, 4, 5
Factors of 15: 1, 3, 5
Common Factors: 1, 5 out of which 5 is the greatest hence it is the GCD.


Solution Approach:

Brute Force Approach: Take the ith counter fact and checked whether it divides both the number or not
Optimal Approach: Find the gcd using Euclidean Algorithm.

'''


def brute_gcd(a, b):

    i = 1
    fact = 1

    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            fact = i

        i += 1

    return fact

print(brute_gcd(9, 12))
print(brute_gcd(20, 15))


def euclidean_gcd(a, b):

    while b > 0:
        a, b = b, a % b

    return a

print(euclidean_gcd(9, 12))
print(euclidean_gcd(20, 15))
