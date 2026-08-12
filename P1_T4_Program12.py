# Check whether a number is a palindrome.

def Palindrome(Num):
    Org = Num 
    Rev = 0
    while (Num > 0):
        Rem = Num % 10
        Num = Num // 10
        Rev = Rev * 10 + Rem

    if (Rev == Org):
        return "Palindrome"
    return "Not Palindrome"

def main():
    Num = int(input("Enter the number : "))

    Ret = Palindrome(Num)

    print(f"The number is {Ret}")

if __name__=="__main__":
    main()