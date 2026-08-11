# Reverse a number.

def Reverse(Num):
    Rev = 0 
    Rem = 0
    while (Num > 0):
        Rem = Num % 10
        Num = Num // 10
        Rev = Rev * 10 + Rem

    return Rev

def main():
    Num = int(input("Enter the number : "))

    Ret = Reverse(Num)

    print(f"The reverse of {Num} is {Ret}")

if __name__=="__main__":
    main()