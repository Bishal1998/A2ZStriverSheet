'''

Problem Statement: Given an array of N integers, write a program to implement the Recursive Insertion Sort algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52

Example 2:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5

Solution Approach: Using the same logic used in the earlier insertion sort program.

'''


def recursive_insertion_sort(arr, i = 0):

    n = len(arr)

    if i == n:
        return arr

    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

    return recursive_insertion_sort(arr, i + 1)

print(recursive_insertion_sort([13,46,24,52,20,9]))