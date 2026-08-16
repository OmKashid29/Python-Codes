# Check whether a number is an Armstrong number.

def Armstrong(Num):
    Org = Num 
    Rev = 0
    while (Num > 0):
        Rem = Num % 10
        Num = Num // 10
        Rev = Rem ** 3 + Rev

    if (Rev == Org):
        return "Armstrong"
    return "Not Armstrong"

def main():
    Num = int(input("Enter the number : "))

    Ret = Armstrong(Num)

    print(f"The number is {Ret}")

if __name__=="__main__":
    main()