'''
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Examples 2:

Input: arr = [1]

Output: 1

Explanation: Array has only one element and which is giving positive sum of 1.

Solution Approach:
We need to find the sum of sub-array and check whether it is greater than the sum stored in the maximum variable. The sub-array sum will be calculated by checking whether sum is less than 0 or not.
'''


def kadane_algorithm(nums):
    maximum = float("-inf")
    s = 0 #sum of the sub-array

    for num in nums:
        s += num
        maximum = max(maximum, s)

        if s < 0:
            s = 0

    return maximum
print(kadane_algorithm([-2,1,-3,4,-1,2,1,-5,4] ))