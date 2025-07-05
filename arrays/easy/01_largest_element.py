
'''

Problem Statement: Given an array, we have to find the largest element in the array.

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array.

Example2:
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array.

Solution Approach :
1. Using the loop and compare with the minimum value i.e. -inf
2. Using the max built-in methods
3. Using built-in sorted method and returning the largest value using slicing

'''

def largest_elem(arr):
    maximum = float('-inf')

    for i in arr:
        if i > maximum:
            maximum = i

    return maximum

print(largest_elem([8,10,5,7,9]))

print(max([2,5,1,3,0]))

def largest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-1]

print(largest([2,5,1,3,0]))
