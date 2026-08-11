# Count digits in a number

def Calculate(Num):
    digits = 0
    while (Num > 0):
        Num = Num // 10
        digits = digits + 1

    return digits

def main():
    Num = int(input("Enter The number : "))

    Ret = Calculate(Num)

    print(f"The number of digits in {Num} are {Ret}")

if __name__=="__main__":
    main()