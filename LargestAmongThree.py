num1=eval(input("Enter 1st Number:"))
num2=eval(input("Enter 2nd Number:"))
num3=eval(input("Enter 3rd Number:"))

if (num1>num2) and (num1>num3):
    print(num1,"is the largest among three.")
elif (num2>num1) and (num2>num3):
    print(num2,"is the largest among three.")
else:
    print(num3,"is the largest among three.")
