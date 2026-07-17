# Check whether a number is even or odd.

def CheckEvenOrOdd(N):
    if N % 2 == 0:
        return True
    return False

def main():
    No = int(input("Enter the number : "))
    Ret = CheckEvenOrOdd(No)

    if Ret == True :
        print(f"{No} is Even")
    else:
        print(f"{No} is Odd")

if __name__=="__main__":
    main()
