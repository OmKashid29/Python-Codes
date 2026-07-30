# Find the largest among four numbers.

def Largest(No1,No2,No3,No4):
    if (No1 > No2 and No1 > No3 and No1 > No4):
        return No1
    elif (No2 > No3 and No2 > No4):
        return No2
    elif (No3 > No4):
        return No3
    else :
        return No4

def main():
    No1 = float(input("Enter the first number : "))
    No2 = float(input("Enter the second number : "))
    No3 = float(input("Enter the third number : "))
    No4 = float(input("Enter the forth number : "))

    Ret = Largest(No1,No2,No3,No4)

    print(f"{Ret} is the largest")

if __name__ == "__main__":
    main()