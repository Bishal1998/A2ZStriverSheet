'''

Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5

Solution Approach: First find the smallest number in the array and swap it with the ith position of the element, like i runs from 0 to n - 1, while, j runs from i + 1 to n, and we we track the minimum element with the index, and if we found smallest element, we swap it.

'''


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([13, 46, 24, 52, 20, 9]))
