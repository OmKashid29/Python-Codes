# Count the number of factors.

def Factors(Num):
    Count = 0
    for i in range(1,Num + 1):
        if (Num % i == 0 ):
            Count = Count + 1

    return Count
            

def main():
    Num = int(input("Enter the number : "))

    Ret = Factors(Num)

    print(f"There are {Ret} factors of number {Num}")

if __name__=="__main__":
    main()