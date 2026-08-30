# Check whether a number is a Happy number.

def Happy(Num,Count):
    Count = Count + 1
    List = []
    while (Num > 0):
        Rem = Num % 10
        Num = Num // 10
        List.append(Rem)

    Sum = 0
    for i in List:
        Sum = Sum + i * i

    if (Sum == 1):
        print("The number is happy number")
    else:
        if(Count > 8):
            print("The number is not happy number")
        else:
            Happy(Sum,Count)
            return

def main():
    Num = int(input("Enter the number : "))
    Count = 0
    Happy(Num,Count)

if __name__=="__main__":
    main()