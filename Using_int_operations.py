def find(num1,num2,num3):
        a= num1<num2  and  num2>=num3
        b= num1>num2 and num2 <=num3
        c= num3 == num1 and num1 != num2
        print(a,b,c)



find(2,6,4)