# Find the LCM of two numbers.

def LCM(N1,N2):

    L1 = N1
    L2 = N2

    while(N1 != N2):
        if (N1 > N2):
            N2 = L2 + N2
        else:
            N1= L1 + N1

    return N1

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = LCM(No1,No2)

    print(f"The LCM of {No1} and {No2} is {Ret}")

if __name__=="__main__":
    main()