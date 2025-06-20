'''

Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Examples:

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

'''


def sum_natural(i, n, sum):
    if i > n:
        return sum
    sum += i
    return sum_natural(i + 1, n, sum)


if __name__ == '__main__':
    sum = 0
    total_sum = sum_natural(1, 5, sum)
    print(total_sum)
