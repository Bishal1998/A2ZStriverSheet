
'''

Print the name n times using recursion.

'''

def print_name(i, n):

    if i > n:
        return

    print("Bishal")
    print_name(i+1, n)

if __name__ == "__main__":

    num = int(input("Enter total number: "))

    print_name(1, num)
