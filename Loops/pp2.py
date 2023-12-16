# for checking leap year..
n = 2020
if (n % 100 == 0 and n % 400 == 0):
    print("century even year")

elif (n % 100 != 0 and n % 4 == 0):
    print("Even year")
else:
    print("not even year")
