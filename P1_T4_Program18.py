# Print all prime numbers between 1 and N.

def Prime(Num):
    List = []
    for n in range(1,Num + 1):
        Count = 0
        for i in range(1,n + 1):
            if(n % i == 0 ):
                Count = Count + 1

        if (Count == 2):
            List.append(n)

    return List
    
def main():
    Num = int(input("Enter the number : "))

    Ret = Prime(Num)

    print(f"The prime numbers for 1 to {Num} are {Ret}")

if __name__=="__main__":
    main()