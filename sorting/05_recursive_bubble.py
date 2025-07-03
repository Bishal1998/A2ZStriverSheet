'''

Prblem Statement: Given an array of N integers, write a program to implement the Recursive Bubble Sort algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52

Example 2:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5

Solution Approach: The logic is same as the Bubble sort what we have to modify is using the
recursion.

'''


def recursive_bubble_sort(arr, i=0):
    n = len(arr)

    swapped = False

    if i == n - 1:
        return arr

    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            swapped = True
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if not swapped:
        return arr
    return recursive_bubble_sort(arr, i + 1)


print(recursive_bubble_sort([13, 46, 24, 52, 20, 9]))
