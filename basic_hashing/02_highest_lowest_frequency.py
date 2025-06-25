'''

Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Examples:

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.


'''

def highest_lowest_frequency(arr):

    freq = {}

    for item in arr:
        freq[item] = freq.get(item, 0) + 1

    # updating the value
    maximum = max(freq.values())
    minimum = min(freq.values())

    # maximum and minimum
    max_elem = None
    min_elem = None

    # extracting the keys from values
    for k, v in freq.items():
        if v == maximum and max_elem is None:
            max_elem = k

        if v == minimum and min_elem is None:
            min_elem = k

    return f"maximum: {max_elem}, minimum : {min_elem}"


nums = [10, 5, 10, 15, 10, 5]
print(highest_lowest_frequency(nums))