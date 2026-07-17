# Find remainder without using %.

def Remainder(N1,N2):
    Q = N1 // N2
    return N1 - Q * N2

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Ret = Remainder(No1,No2)
    print(f"the remainder after {No1} divided by {No2} is {Ret}")

if __name__=="__main__":
    main()
