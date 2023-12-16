with open("this.txt")as s:
    content = s.read()

with open("copy.txt", "w")as f:
    f.write(content)
