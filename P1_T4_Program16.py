# Check whether a number is a Perfect number.

def Perfect(Num):
    Sum = 0

    for i in range(1,Num):
        if (Num % i == 0):
            Sum = Sum + i

    if (Sum == Num):
        return "Perfect"
    return " Not Perfect"

def main():
    Num = int(input("Enter the number : "))

    Ret = Perfect(Num)

    print(f"The number is {Ret}")

if __name__=="__main__":
    main()