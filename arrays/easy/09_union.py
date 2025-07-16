'''

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in the union should be in ascending order.

Example 1:
Input:
n = 5,m = 5.
arr1[] = {1,2,3,4,5}
arr2[] = {2,3,4,4,5}
Output:
 {1,2,3,4,5}

Explanation:
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5}

Example 2:
Input:
n = 10,m = 7.
arr1[] = {1,2,3,4,5,6,7,8,9,10}
arr2[] = {2,3,4,4,5,11,12}
Output: {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation:
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}

Solution:
1. Convert the arr to set and use the built-in union methods and then finally return the sorted array.
2. Similar to merge sort for the merging part but we need to check for the duplicate element using set.

'''


def union(arr_a, arr_b):

    merge = sorted(set(arr_a).union(set(arr_b)))

    return merge

print(union([1,2,3,4,5], [2,3,4,4,5]))

def union(arr_a, arr_b):

    i = j = 0

    a = len(arr_a)
    b = len(arr_b)

    result = []
    unique = set()

    while i < a and j < b:

        if arr_a[i] < arr_b[j]:
            if arr_a[i] not in unique:
                unique.add(arr_a[i])
                result.append(arr_a[i])
            i += 1
        elif arr_a[i] > arr_b[j]:
            if arr_b[j] not in unique:
                unique.add(arr_b[j])
                result.append(arr_b[j])
            j += 1
        else:
            if arr_a[i]  not in unique:
                unique.add(arr_a[i])
                result.append(arr_a[i])
            i += 1
            j += 1

    while i < a:
        if arr_a[i] not in unique:
            unique.add(arr_a[i])
            result.append(arr_a[i])
        i += 1

    while j < b:
        if arr_b[j] not in unique:
            unique.add(arr_b[j])
            result.append(arr_b[j])
        j += 1

    return result

print(union([1,1,2,3,4,5], [2,3,4,4,4,5,6]))


