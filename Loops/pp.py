
n = int(input("enter the number "))

if (n % 2 != 0):
    print("weird")

elif (n % 2 == 0) and (n >= 2 and n <= 5):
    print("Not weird")

elif (n % 2 == 0) and (n >= 6 and n <= 20):
    print("weird")

elif n < 20:
    print("Not weird")
