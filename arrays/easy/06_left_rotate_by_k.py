
'''

Rotate array by K elements

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.


Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

Solution Approach: Using slicing
'''

def left_rotate_k(nums, k):
    n = len(nums)

    k = k % n

    return nums[-k:] + nums[:-k]

print(left_rotate_k([1,2,3,4,5], 3))