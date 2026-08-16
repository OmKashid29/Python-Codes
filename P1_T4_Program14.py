# Check whether a number is a Strong number.

def Strong(Num):
    Org = Num 
    Fact = 1
    Total = 0
    while (Num > 0):
        Rem = Num % 10
        Num = Num // 10
        for i in range(1,Rem + 1):
            Fact = Fact * i

        Total = Fact + Total
        Fact = 1

    if (Total == Org):
        return "Strong"
    return "Not Strong"

def main():
    Num = int(input("Enter the number : "))

    Ret = Strong(Num)

    print(f"The number is {Ret}")

if __name__=="__main__":
    main()