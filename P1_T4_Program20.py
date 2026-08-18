# Find the GCD of two numbers.

def GCD(N1,N2):
   
    while(N1 != N2):
        if (N1 > N2):
            N1 = N1 - N2
        else:
            N2 = N2 - N1

    return N1

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = GCD(No1,No2)

    print(f"The GCD of {No1} and {No2} is {Ret}")

if __name__=="__main__":
    main()