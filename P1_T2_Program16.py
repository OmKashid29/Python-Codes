# Reverse a three-digit number (without loops).

def Reverse(N):
    Units = N % 10
    Tens = (N // 10) % 10
    Hundred = N // 100

    reverse = Hundred  + Tens * 10 + Units * 100
    return reverse

def main():
    No = int(input("Enter the number : "))
    Ret = Reverse(No)
    print(f"The reverse of {No} is {Ret}")

if __name__=="__main__":
    main()