text = input("Enter your text\n")

if("makes a lot of money" in text):
    a = True
elif("buy now" in text):
    a = True
elif("click this" in text):
    a = True
elif("subscribe this" in text):
    a = True
else:
    a = False

if(a):
    print("this is spam")
else:
    print("this is not spam")
