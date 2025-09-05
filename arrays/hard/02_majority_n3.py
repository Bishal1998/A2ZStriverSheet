'''

Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.

Example 1:
Input Format: N = 5, array[] = {1,2,2,3,2}
Result: 2
Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

Example 2:
Input Format:  N = 6, array[] = {11,33,33,11,33,11}
Result: 11 33
Explanation: Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.


Solution Approach:  We can solve it using Hashmap but it will take extra space, so to solve it in O(1), we can use the same approach as in n/2 i.e Boyer-Moore Algorithm.

'''



def majority_n3(nums):

    count1, count2 = 0, 0
    candidate1, candidate2 = None, None


    for num in nums:

        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1


    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1


    res = []
    n = len(nums)

    if count1 > n // 3:
        res.append(candidate1)
    if count2 > n // 3:
        res.append(candidate2)


    return res


print(majority_n3([11,33,33,11,33,11]))