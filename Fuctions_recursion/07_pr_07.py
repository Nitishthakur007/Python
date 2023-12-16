def remove_and_split(string, word):
    newstr = string.replace(word, "our")
    return newstr.strip()


state = "    This is my world    "
n = remove_and_split(state, "my")
print(n)


#a = "    hello here     "
# print(a.strip())
