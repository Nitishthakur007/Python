words = ["donkey", "kaddu", "mote"]

with open("xample.txt")as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#%@!$*^")
    with open("xample.txt", "w")as f:
        f.write(content)
