
'''

Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.

Solution Approach:
1. first sort the elements using sort() methods and access the second minimum and maximum using slicing, but this is not a good idea to return the value using constant as it will not satisfy the inputs like [1,1]

2. first finding the maximum and minimum value and then find the second maximum and minimum comapring with the minimum and maximum value.


'''
my_list = [1,2]

# def smallest_largest(arr):
#
#     new_arr = list(set(arr))
#     new_arr.sort()
#     if len(arr) < 2:
#         return f"Second maximum: -1, second minimum: -1"
#
#     return f"Second maximum: {new_arr[-2]}, second minimum: {new_arr[1]}"
#
# print(smallest_largest(my_list))


def largest_smallest(arr):

    maximum = second_maximum = float('-inf')
    minimum = second_minimum =  float('inf')

    if len(set(arr)) < 2:
        return f"Second maximum: -1, second minimum: -1"

    for num in arr:
        if num > maximum:
            second_maximum = maximum
            maximum = num
        elif maximum > num > second_maximum:
            second_maximum = num

        if num < minimum:
            second_minimum = minimum
            minimum = num
        elif minimum < num < second_minimum:
            second_minimum = num

    if second_maximum == float('-inf'):
        second_maximum = -1
    if second_minimum == float('inf'):
        second_minimum = -1

    return f"Second maximum: {second_maximum}\nSecond minimum: {second_minimum}"

print(largest_smallest(my_list))