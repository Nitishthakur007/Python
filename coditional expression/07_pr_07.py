post = input("Write your post here\n")
if "harry" in post:
    print("This post is about harry")
elif "HARRY" in post:
    print("This post is about harry")
elif "Harry" in post:
    print("This post is about harry")
elif "HaRRY" in post:
    print("This post is about harry")
else:
    print("This post is not about harry")
print("done")
