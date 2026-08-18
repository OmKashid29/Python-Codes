# Print the Fibonacci series.

def Fibonacci(Num):
    Fibo = [0,1]
    f = 0 
    f0 = 0
    f1 = 1
    
    for i in range(3,Num + 1):
    
        f = f0 + f1
        Fibo.append(f)
        f0 = f1
        f1 = f
        

    return Fibo

def main():
    Num = int(input("Enter the number : "))

    Ret = Fibonacci(Num)

    print(f"The fibonacci series till first {Num} number is {Ret}")

if __name__=="__main__":
    main()