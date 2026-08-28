# Find the sum of the Fibonacci series up to N terms.

def Fibonacci(N):
    Sum = 1
        
    f = 0 
    f0 = 0
    f1 = 1
        
    for i in range(3,N + 1):

        f = f0 + f1
        Sum = Sum + f
        f0 = f1
        f1 = f

    return Sum

def main():
    Num = int(input("Enter the number : "))

    Ret = Fibonacci(Num)

    print(f"The sum of fibonacci series from 1 to {Num} number is {Ret}")

if __name__=="__main__":
    main()