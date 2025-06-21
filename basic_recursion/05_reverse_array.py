

'''

Problem Statement: You are given an array. The task is to reverse the array and print it.

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}

Solution Approach:

1. First using slicing
2. Using loop
3. Using recursion

'''
my_array = [1, 2, 3, 4, 5]

def reverse_slicing(arr):
    return arr[::-1]

print(reverse_slicing(my_array))


def reverse_loop(arr):
    new_list = []
    for i in range(len(arr) - 1, -1, -1):
        new_list.append(arr[i])

    return new_list

print(reverse_loop(my_array))


def reverse_recursion(arr, start, end):

    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverse_recursion(arr, start + 1, end - 1)

    return arr

if __name__ == "__main__":
    print(reverse_recursion(my_array, 0, len(my_array) - 1))