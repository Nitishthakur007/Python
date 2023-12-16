letter = '''Dear <|NAME|>
you are selected
Date: <|DATE|>
'''
name = input("Enter your name here")
date = input("enter date here")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
