
'''
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

Example 2:

Input: nums=[-1,0,1,0]
Output: Output: [[-1,0,1],[-1,1,0]]
Explanation: Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k

'''

def three_sum(nums):

    nums.sort()

    ans = []
    n = len(nums)

    for i in range(n):

        if nums[i] > 0:
            break

        elif i != 0 and nums[i] == nums[i - 1]:
            continue

        lo, hi = i + 1, n - 1

        while lo < hi:

            summ = nums[i] + nums[lo] + nums[hi]

            if summ == 0:
                ans.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1

                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif summ < 0:
                lo += 1
            else:
                hi -= 1

    return ans


print(three_sum([-1,0,1,2,-1,-4]))