# Reverse a two-digit number.

def Reverse(N):
    N = abs(N)
    Rev = 0

    while(N != 0):
        Rem = N % 10
        N = N // 10
        Rev = Rev * 10 + Rem

    return Rev

def main():
    No = int(input("Enter the number : "))
    Ret = Reverse(No)
    print(f"The reverse of {No} is {Ret}")

if __name__=="__main__":
    main()