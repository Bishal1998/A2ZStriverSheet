
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
1. Using triple nested loops to generate all the sub-array and checked whether the sum of the sub array is equal to the given sum K, if equals save the maximum length of the sub-array. O(n3)
2. Using nested loops and this will reduce the complexity to O(n^2)





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


def longest_subarray(arr, K):
    length = 0

    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]

            if s == K:
                length = max(length, j - i + 1)

    return length

print(longest_subarray([2,3,5,1,9], 10))


def longest_subarray_sum(arr, K):

    length = 0
    prefix_sum = 0
    sum_indices = {}

    for i in range(0, len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == K:
            length = i + 1

        if prefix_sum - K in sum_indices:
            length = max(length, i - sum_indices[prefix_sum - K])

        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i

    return length

print(longest_subarray_sum([10, -10, 20, 30], 5))


