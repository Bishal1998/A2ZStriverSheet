
'''

Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

Solution Approach:
1. Using triple nested loops to generate all the sub-array and checked whether the sum of the sub array is equal to the given sum K, if equals save the maximum length of the sub-array.



'''


def brute_longest_subarray(arr, K):

    length = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            s = 0
            for k in range(i, j + 1):
                s += arr[k]

            if s == K:
                length = max(length, j - i + 1)


    return length


print(brute_longest_subarray([2,3,5,1,9], 10))