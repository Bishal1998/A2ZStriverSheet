'''

Problem:  Given an array of size n, sort the array using Merge Sort.

Example 1:
Input: N=5, arr[]={4,2,1,6,7}
Output: 1,2,4,6,7,


Example 2:
Input: N=7,arr[]={3,2,8,5,1,4,23}
Output: 1,2,3,4,5,8,23

Solution Approach: Use the recursion, first divide the array into two halves, and
repeat this division until all the elements are divided and results in a single array using recursive calls,
then merge them by comparing together and returns the arr after being sorted

'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    result = []

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result


arr = [3, 2, 8, 5, 1, 4, 23]
new_arr = merge_sort(arr)
print(new_arr)
