

'''

Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.

Example 1:
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

Example 2:
Input Format: A = [5, 6, 7, 8, 9], k = 5
Result: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]


'''

def count_xor(nums, k):


    hashmap = {}
    prefix_xor = 0
    count = 0


    for num in nums:

        prefix_xor ^= num

        if prefix_xor == k:
            count += 1

        if prefix_xor ^ k in hashmap:
            count += hashmap[prefix_xor ^ k]

        hashmap[prefix_xor] = hashmap.get(prefix_xor, 0) + 1

    return count


print(count_xor([4, 2, 2, 6, 4], 6))