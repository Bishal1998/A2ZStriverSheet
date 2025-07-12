
"""
Move all Zeros to the end of the array

Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Solution:
1. Using nested loops
2. Using temp variable
3. Using two-pointer

"""


def move_zero(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] != 0:
                break
            if arr[i] == 0 and arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return arr

print(move_zero([1, 0, 2, 3, 0, 4, 0, 1]))


def move_zero(arr):
    temp = []

    n = len(arr)
    count = 0

    for num in arr:
        if num != 0:
            temp.append(num)
            count += 1

    for i in range(n - count):
        temp.append(0)

    return temp

print(move_zero([1, 0, 2, 3, 0, 4, 0, 1]))

def move_zero(arr):
    n = len(arr)
    j = -1

    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    if j == -1:
        return

    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

print(move_zero([1, 0, 2, 3, 0, 4, 0, 1]))
