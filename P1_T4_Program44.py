# Generate the Collatz sequence for a number.

def Collatz(Num):
    if (Num % 2 == 0):
        Num = Num // 2
        print(Num)
        if(Num != 1):
            Collatz(Num)
            return 
    else:
        Num = 3 * Num + 1
        print(Num)
        Collatz(Num)
        return

def main():
    Num = int(input("Enter the number : "))

    Collatz(Num)

if __name__=="__main__":
    main()