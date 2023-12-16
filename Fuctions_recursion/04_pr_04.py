# sum of n  natural numbers

def sum_recursive(n):
    if n == 1:
        return 1
    return n+sum_recursive(n-1)


num = int(input("Enter the number"))
print(sum_recursive(num))
