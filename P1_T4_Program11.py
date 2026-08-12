# Find factorial of a number

def Factorial(Num):
    Fact = 1

    for i in range(1,Num + 1):
        Fact = Fact * i

    return Fact

def main():
    Num = int(input("Enter the number : "))

    Ret = Factorial(Num)

    print(f"The factorial of the {Num} is {Ret}")

if __name__=="__main__":
    main()