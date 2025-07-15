'''
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Examples:

Example 1:

Input: prices = {1, 1, 0, 1, 1, 1}

Output: 3

Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Input: prices = {1, 0, 1, 1, 0, 1}

Output: 2

Explanation: There are two consecutive 1's in the array.

Solution : We need to increment the count value if the number is one and reset the count to 0 if 1 is not in the num, then we need to update the max_consecutive of 1 as: max(max_consecutive, count)

'''


def maximum_consecutive(arr):
    max_consecutive = 0
    count = 0

    for num in arr:
        if num == 1:
            count += 1
        else:
            count = 0
        max_consecutive = max(max_consecutive, count)

    return max_consecutive


print(maximum_consecutive([1, 0, 1, 1, 0, 1]))
