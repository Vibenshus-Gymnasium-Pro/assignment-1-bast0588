numbers = [num for num in range (1,10)]
for x in numbers:
    if (x > 3):
        print(f"{x}th")
    elif(x == 3):
        print(f"{x}rd")
    elif(x == 2):
        print(f"{x}nd")
    elif(x == 1):
        print(f"{x}st")