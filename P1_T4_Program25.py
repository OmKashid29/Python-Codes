# Find the smallest digit in a number.

def Calculate(Num):
    N1 = 9 

    while(Num > 0):
        N2 = Num % 10
        Num = Num // 10
        if (N2 < N1):
            N1 = N2

    return N1

def main():
    Num = int(input("Enter the number : "))

    Ret = Calculate(Num)

    print(f"The smallest digit of number {Num} is {Ret}")

if __name__=="__main__":
    main()