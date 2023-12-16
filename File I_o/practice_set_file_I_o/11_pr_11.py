import os  # import os module

with open("samp.txt")as f:
    content = f.read()

with open("renamed_by_python.txt", "w")as f:
    f.write(content)

os.remove("samp.txt")  # deleting file with the help of os
