
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

