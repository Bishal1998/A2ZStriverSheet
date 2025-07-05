'''

Problem Statement:  Given an array of n integers, sort the array using the Quicksort method.

Examples:

Example 1:
Input:  N = 5  , Arr[] = {4,1,7,9,3}
Output: 1 3 4 7 9

Explanation: After sorting the array becomes 1, 3, 4, 7, 9

Example 2:
Input: N = 8 , Arr[] = {4,6,2,5,7,9,1,3}
Output: 1 2 3 4 5 6 7 9
Explanation: After sorting the array becomes 1, 3, 4, 7, 9

Solution Approach: Using recursion and it is divide and conquer method.

'''



def quick_sort(arr, low, high):

    if low >= high:
        return
    pivot = recursive_quick_sort(arr, low, high)
    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)
    return arr


def recursive_quick_sort(arr, low, high):

    left = low + 1
    right = high

    pivot_elem = arr[low]

    while True:
        while left <= right and arr[left] <= pivot_elem:
            left += 1
        while left <= right and arr[right] > pivot_elem:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

print(quick_sort([2, 6, 5, 3, 8, 7, 1, 0], 0, 7))
