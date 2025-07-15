'''
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

Solution: Find the value that exists just one time in the array and for that we can use dictionary.

'''


def find_one(nums):
    my_dict = {}

    for num in nums:
        my_dict[num] = my_dict.get(num, 0) + 1

    for key, values in my_dict.items():
        if values == 1:
            return key
    return None
print(find_one([2,2,1,1,3]))