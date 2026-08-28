# Find the sum of factorials from 1 to N.

def Factorial(Num):
    Sum = 0
    for N in range(1,Num + 1):
        Fact = 1

        for i in range(1,N + 1):
            Fact = Fact * i

        Sum = Sum + Fact

    return Sum

def main():
    Num = int(input("Enter the number : "))

    Ret = Factorial(Num)

    print(f"The sum of factorials from 1 to {Num} is {Ret}")

if __name__=="__main__":
    main()