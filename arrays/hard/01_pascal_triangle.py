'''
Problem Statement: This problem has 3 variations. They are stated below:

Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

In Pascal’s triangle, each number is the sum of the two numbers directly above it
'''


def pascal_triangle(n):
    ans_list = []

    for row in range(n):
        temp = []
        ans = 1
        for col in range(row + 1):
            if col == 0:
                temp.append(1)
            else:
                ans = ans * (row - col + 1)
                ans = ans // col
                temp.append(ans)
        ans_list.append(temp)

    return ans_list

print(pascal_triangle(5))

