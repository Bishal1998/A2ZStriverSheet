
'''
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]

Output: [[7,4,1],[8,5,2],[9,6,3]]

Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.

Example 2:

Input: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

Output:[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix

Solution Approach:
1. Transpose the matrix
2. Reverse each row
'''

def rotate_image(arr):
    n = len(arr)


    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(n):
        arr[i].reverse()

    return arr
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate_image(matrix))
