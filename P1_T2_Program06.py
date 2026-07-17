# Calculate the power of a number

def Power(B,E):
    return B**E    

def main():
    Base = float(input("Enter the base number : "))
    Exponient = float(input("Enter the exponient number : "))

    Ret = Power(Base,Exponient)

    print(f"The power is {Ret}")

if __name__=="__main__":
    main()
