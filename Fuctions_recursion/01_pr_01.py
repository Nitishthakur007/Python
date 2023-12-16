def maximum(num1, num2, num3):
    if (num1 > num2):
        if(num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num2 < num1):
            return num2
        else:
            return num3


m = maximum(6, 5, 8)
print(m)


s = maximum(58, 8, 235)
print(s)
