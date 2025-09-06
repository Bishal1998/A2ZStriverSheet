

'''

Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.


Example 1:
Input Format: arr[] = [1,0,-1,0,-2,2], target = 0
Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Explanation: We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. The result obtained is such that the sum of the quadruplets yields 0.

Example 2:
Input Format: arr[] = [4,3,3,4,4,2,1,2,1,1], target = 9
Result: [[1,1,3,4],[1,2,2,4],[1,2,3,3]]
Explanation: The sum of all the quadruplets is equal to the target i.e. 9.

'''


def four_sum(arr, k):

    arr.sort()
    n = len(arr)
    res = []

    for i in range(n):

        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):

            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            lo, hi = j + 1, n - 1

            while lo < hi:

                summ = arr[i] + arr[j] + arr[lo] + arr[hi]

                if summ == k:
                    res.append([arr[i], arr[j], arr[lo], arr[hi]])

                    lo += 1
                    hi -= 1

                    while lo < hi and arr[lo] == arr[lo - 1]:
                        lo += 1

                    while lo < hi and arr[hi] == arr[hi + 1]:
                        hi -= 1

                elif summ < k:
                    lo += 1
                else:
                    hi -= 1

    return res


print(four_sum([1,0,-1,0,-2,2], 0))
