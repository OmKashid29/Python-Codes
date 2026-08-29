# Print all factors of a number.

def Factors(Num):
    for i in range(1,Num + 1):
        if (Num % i == 0 ):
            print(i)

def main():
    Num = int(input("Enter the number : "))

    Factors(Num)

if __name__=="__main__":
    main()