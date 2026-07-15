# Find the first digit of a number.

def Calculate(N):
    N = abs(N)
    while(N != 0 ):
        Rem = N % 10
        N = N // 10

    return Rem

def main():
    No = int(input("Enter the number : "))

    Ret = Calculate(No)

    print("The first digit of the number is : ",Ret)

if __name__=="__main__":
    main()