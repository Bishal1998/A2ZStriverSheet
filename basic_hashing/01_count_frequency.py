'''

Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Examples:

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	    5  2
        15  1
Explanation: 10 occurs 3 times in the array
	         5 occurs 2 times in the array
             15 occurs 1 time in the array

Example2:
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	    3  1
        4  2
Explanation: 2 occurs 3 times in the array
	         3 occurs 1 time in the array
             4 occurs 2 time in the array

Solution: Creating a freq dict and check whether the number already exist in the dict or not, if exists then increment the frequency else keep the value as 1.
 We can write this:

    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

as: freq[num] = freq.get[num, 0] + 1

'''


def count_frequency(arr):

    freq = {}

    for item in arr:
        freq[item] = freq.get(item, 0) + 1

    return freq

nums = [10,5,10,15,10,5]
print(count_frequency(nums))