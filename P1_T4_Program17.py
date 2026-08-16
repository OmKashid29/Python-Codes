# Check whether a number is a Prime number.

def Prime(Num):
    Count = 0
    for i in range(1,Num + 1):
        if(Num % i == 0 ):
            Count = Count + 1
    
    if Count == 2 :
        return "Prime"
    return "Not Prime"

def main():
    Num = int(input("Enter the number : "))

    Ret = Prime(Num)

    print(f"The number is {Ret}")

if __name__=="__main__":
    main()