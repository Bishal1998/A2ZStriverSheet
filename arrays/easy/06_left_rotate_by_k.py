
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


def reverse(arr):
    # reverse_arr = []
    # for i in range(len(arr) - 1, -1, -1):
    #     reverse_arr.append(arr[i])
    #
    # return reverse_arr

    # reverse_arr = list( reversed(arr))
    # return reverse_arr

    return arr[::-1]

    # left, right = 0, len(arr) - 1
    #
    # while left < right:
    #     arr[left], arr[right] = arr[right], arr[left]
    #     left += 1
    #     right -= 1
    #
    # return arr

# print(reverse([1,2,3,4,5]))

def reverse_two(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

def rotate_reverse(arr, k):
    k = k % len(arr)

    reverse_two(arr, 0, len(arr) - 1)
    reverse_two(arr, 0, k - 1)
    reverse_two(arr, k, len(arr) - 1)


    return arr

print(rotate_reverse([1,2,3,4,5], 3))