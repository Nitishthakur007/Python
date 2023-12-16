# TO FIND OUT WHETHER A FILE IS IDENTICAL AND
# MATCHES THE CONTENT OF ANOTHER

file1 = "this.txt"
file2 = "copy.txt"

with open(file1)as f:
    f1 = f.read()

with open(file2)as f:
    f2 = f.read()

if f1 == f2:
    print("this file is identical")

else:
    print("this file is not identical")
