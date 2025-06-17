

'''

Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Example 1:

Input:N = 153
Output:True

Explanation: 13+53+33 = 1 + 125 + 27 = 153

Example 2:

Input:N = 371
Output: True

Explanation: 33+53+13 = 27 + 343 + 1 = 371


Solution Approach : First count the number of digits in the integer and then check the sum of the power of each digit and total digits and compared it with the original number.

Also, we can convert the given integer into string to use the len function to find the total digit as : counter = len(str(integer)), so that we do not need to create separate function for the counter

'''

integer = 9424

# def count_digits(n):
#     count = 0
#
#     while n > 0:
#         n = n // 10
#         count += 1
#
#     return count
#
# counter = count_digits(integer)

counter = len(str(integer))

def armstrong_number(n, count):

    num = n
    sum = 0


    while n > 0:

        rem = n % 10
        sum += rem ** count
        n = n // 10

    return True if sum == num else False


print(armstrong_number(integer, counter))