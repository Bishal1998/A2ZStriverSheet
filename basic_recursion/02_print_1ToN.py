'''

Problem Statement: Print 1 to N using Recursion

'''


def print_to_n(i, n):
    if i > n:
        return

    print(i)
    print_to_n(i + 1, n)

if __name__ == '__main__':
    num = int(input("Enter number: "))

    if num <= 0:
        print("Invalid input")
    else:
        print_to_n(1, num)