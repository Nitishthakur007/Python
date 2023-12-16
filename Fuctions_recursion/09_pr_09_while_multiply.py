def multiplication(num):
    i = 1
    while i <= 10:
        print(f"{num}x{i}={num*i}")
        i = i+1


num = int(input("Enter the number here"))
s = multiplication(num)
print(s)
