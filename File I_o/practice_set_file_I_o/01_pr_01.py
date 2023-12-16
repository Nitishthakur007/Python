from os import read


f = open("poems.txt")
a = f.read()
if "twinkle" in a:
    print("yes")
else:
    print("no")
f.close()
