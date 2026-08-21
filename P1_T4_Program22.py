# Calculate the sum of digits.

def Calculate(Num):
    Sum = 0

    while(Num > 0):
        Rem = Num % 10
        Num = Num // 10
        Sum = Sum + Rem

    return Sum

def main():
    Num = int(input("Enter the number : "))

    Ret = Calculate(Num)

    print(f"The sum of the digits of number {Num} is {Ret}")

if __name__=="__main__":
    main()