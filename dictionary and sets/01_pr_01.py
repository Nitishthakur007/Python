mydict = {
    "deewar": "wall",
    "pankha": "fan",
    "kitaab": "book"
}
a = input("enter your hindi word here,\n")
#print("meaning of your word is", mydict[a])
print("meaning of your word is", mydict.get(a))
