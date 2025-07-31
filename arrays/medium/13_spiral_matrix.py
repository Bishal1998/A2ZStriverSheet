
'''
Problem Statement: Given a Matrix, print the given matrix in spiral order.

Example 1:
Input: Matrix[][] = { { 1, 2, 3, 4 },
		      { 5, 6, 7, 8 },
		      { 9, 10, 11, 12 },
	              { 13, 14, 15, 16 } }

Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.

Example 2:
Input: Matrix[][] = { { 1, 2, 3 },
	              { 4, 5, 6 },
		      { 7, 8, 9 } }

Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
Explanation: The output of matrix in spiral form.
'''

def spiral_matrix(arr):
    l, r = 0, len(arr[0])
    t, b = 0, len(arr)

    res = []

    while l < r and t < b:

        for i in range(l, r):
            res.append(arr[t][i])
        t += 1

        for i in range(t, b):
            res.append(arr[i][r - 1])
        r -= 1

        if not (l < r and t < b):
            break

        for i in range(r - 1, l - 1, -1):
            res.append(arr[b - 1][i])
        b -= 1

        for i in range(b - 1, t - 1, -1):
            res.append(arr[i][l])
        l += 1

    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(spiral_matrix(matrix))