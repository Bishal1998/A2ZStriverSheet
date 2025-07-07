'''

Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.

Here element 5 is not smaller than or equal to its future elements.

Solution Approach:
1. Using the built-in sorted() methods, it has time complexity - 0(n log n) as sorted() has 0(n log n)
2. Using loops has 0(n) complexity

'''

# def check_sorted(arr):
#     return sorted(arr) == arr


def check_sorted(arr):

    if len(arr) <= 1:
        return True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True

# Test cases
my_list = []
print(check_sorted(my_list))  # True
print(check_sorted([1, 2, 3, 4, 5]))  # True
print(check_sorted([5, 4, 6, 7, 8]))  # False
print(check_sorted([1]))  # True
print(check_sorted([1, 1, 1]))  # True
print(check_sorted([5, 4, 3, 2, 1]))  # False
print(check_sorted([1, 1, 2, 2]))  # True