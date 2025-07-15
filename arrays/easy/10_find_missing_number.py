'''
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
Explanation: In the given array, number 2 is missing. So, 2 is the answer.

Solution Approach: Find the total sum of the natural number and then the sum of the elements and finally we can subract them to get the missing number.
'''


def missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2

    num_sum = 0
    for num in nums:
        num_sum += num

    return total_sum - num_sum


print(missing_number([1, 2, 4, 5]))
