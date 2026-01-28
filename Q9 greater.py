a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a >= b and a >= c:
    print("largest number:", a)
elif b >= a and b >= c:
    print("largest number:", b)
else:
    print("largest number:", c)


