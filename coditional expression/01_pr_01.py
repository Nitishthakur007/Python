num1 = int(input("enter number 1 here\t"))
num2 = int(input("enter number 2 here\t"))
num3 = int(input("enter number 3 here\t"))
num4 = int(input("enter number 4 here\t"))

if num1 > num4:
    f1 = num1
else:
    f1 = num4

if num2 > num3:
    f2 = num2
else:
    f2 = num3

if f1 > f2:
    print(str(f1) + " is greatest")

else:
    print(str(f2) + " is greatest")
