'''

Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

Examples 1:

Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

Solution Approach:
1. Brute Force : Time: O(n^3), Space: O(1)
2. Better: Time: O(n^2), Space: O(n) + O(m)
3. Optimal: Time: O(n^2), Space: O(1)

'''

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

row = len(matrix)
column = len(matrix[0])
def set_matrix_zeros():
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                mark_row(i)
                mark_column(j)

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix

def mark_row(i):
    for j in range(column):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def mark_column(j):
    for i in range(row):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


# print(set_matrix_zeros())


def set_0_matrix(arr):
    r = [0] * len(arr)
    c = [0] * len(arr[0])

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                r[i] = 1
                c[j] = 1

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if r[i] or c[j] == 1:
                arr[i][j] == 0

    return arr

# print(set_0_matrix(matrix))

def optimal_set_matrix(arr):

    col0 = 1

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                arr[i][0] = 0

                if j != 0:
                    arr[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            if arr[i][j] != 0:
                if arr[0][j] == 0 or arr[i][0] == 0:
                    arr[i][j] = 0



    if matrix[0][0] == 0:
        for j in range(len(arr[0])):
            arr[0][j] = 0

    if col0 == 0:
        for i in range(len(arr)):
            arr[i][0] = 0

    return arr

print(optimal_set_matrix(matrix))



