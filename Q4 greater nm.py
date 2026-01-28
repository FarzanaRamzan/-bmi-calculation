num1= int(input("enter a number"))
num2 = int(input("enter a number"))
if num1 > num2:
    print("a, greater number")
    if num2 > num1:
        print("b, less number")
    else:
        print("show both number")