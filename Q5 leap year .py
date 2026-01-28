year = int(input("enter ayear"))
if ( year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not leap year")
