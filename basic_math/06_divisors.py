'''

Problem Statement: Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Example 1:

Input:N = 36
Output:[1, 2, 3, 4, 6, 9, 12, 18, 36]

Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Example 2:

Input:N =12
Output: [1, 2, 3, 4, 6, 12]

Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.


Solution Approach:

Brute Force: append the list of the integers that provides 0 remainder while dividing the original number.
Optimized Version : Use the set to remove duplicates and no need to track upto n digits, track till it's perfect square roots and
store the 2 digits at once like:

i = 1, 36 // 1 -> so store 1 and 36, similarly 2 and 18, likewise 6,6 so to remove duplicates we need set.

'''

def divisors(n):
    divisors_list = []
    i = 1

    while i <= n:
        if n % i == 0:
            divisors_list.append(i)
        i += 1
    return divisors_list


def optimized_divisors(n):
    divisors_set = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_set.add(i)
            divisors_set.add(n // i)

    return sorted(divisors_set)

print(divisors(36))
print(optimized_divisors(36))