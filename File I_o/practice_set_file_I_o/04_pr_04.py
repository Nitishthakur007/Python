with open("xample.txt")as f:
    content = f.read()

# if "donkey" in content:
#    with open("xample.txt", "w")as f:
#        content = f.write(content.replace("donkey", "@#$@#$%^"))


content = content.replace("donkey", "#%@!$*^")
with open("xample.txt", "w")as f:
    f.write(content)
