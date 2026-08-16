# Check whether a number is a Neon number.

def Neon(Num):
    Square = Num * Num
    Sum = 0

    while (Square > 0):
        Rem = Square % 10
        Square = Square // 10
        Sum = Sum + Rem

    if (Sum == Num):
        return "Neon"
    return " Not Neon"

def main():
    Num = int(input("Enter the number : "))

    Ret = Neon(Num)

    print(f"The number is {Ret}")

if __name__=="__main__":
    main()