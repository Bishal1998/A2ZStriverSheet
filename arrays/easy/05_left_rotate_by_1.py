
'''

Problem Statement: Given an array of N integers, left rotate the array by one place.

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
Explanation:
Since all the elements in array will be shifted
toward left by one so ‘2’ will now become the
first index and and ‘1’ which was present at
first index will be shifted at last.


Example 2:
Input: N = 1, array[] = {3}
Output: 3
Explanation: Here only element is present and so
the element at first index will be shifted to
last index which is also by the way the first index.


Solution Approach: initialize the first element to temp variable, so that we can assign that variable to the last element and loop through the other elements using arr[i] = arr[i+1]

'''

def left_rotate_1(arr):

    if not arr:
        return arr
    temp = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[len(arr) - 1] = temp
    return arr


print(left_rotate_1([]))
