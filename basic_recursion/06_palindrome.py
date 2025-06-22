'''

Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.


Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.

Solution Approach: Brute Force approach and then recursion.

arr[start] == arr[end] we need to check this, and if this satisfies over the different character, the string must be palindrome else not.


'''
my_string = "ABCDXBA"

def check_palindrome(arr, start, end):

    while start < end:
        if arr[start] == arr[end]:
            start += 1
            end -= 1
        else:
            return False
    return True



print(check_palindrome(my_string, 0, len(my_string) - 1))

def palindrome_recursion(arr, start, end):

    if arr[start] != arr[end]:
        return False

    if start < end:
        return palindrome_recursion(arr, start + 1, end - 1)
    return True


print(palindrome_recursion(my_string, 0, len(my_string) - 1))

