'''
Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input Format: N = 4, array[] = {3, 1, 2, 4}, k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

Example 2:
Input Format: N = 3, array[] = {1,2,3}, k = 3
Result: 2
Explanation: The subarrays that sum up to 3 are [1, 2], and [3].

'''


def sum_k(nums, k):
    count = 0
    hashmap = {}
    total_sum = 0

    for i in range(len(nums)):
        total_sum += nums[i]

        if total_sum == k:
            count += 1

        if (total_sum - k) in hashmap:
            count += hashmap[total_sum - k]

        hashmap[total_sum] = hashmap.get(total_sum, 0) + 1

    return count


print(sum_k([3, 1, 2, 4], 6))
