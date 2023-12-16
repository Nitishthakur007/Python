sub1 = int(input("enter subject 1 marks here "))
sub2 = int(input("enter subject 2 marks here "))
sub3 = int(input("enter subject 3 marks here "))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("you are fail, because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail,due to total percentage less than 40")
else:
    print("congratulations! you are passed")
