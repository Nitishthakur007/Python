# for loop with  else
l = [1, 4, 6, 5]
for item in l:
    print(item)
else:
    print("Done")

# The break statement
for i in range(0, 81):
    print(i)
    if i == 4:
        break

# The continue statement
for i in range(11):
    if i == 5:
        continue
    print(i)


# pass statement
a = [1, 4, 5, 6]
for item in a:
    pass
print("Done")
