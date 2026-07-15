# Find the last digit of a number.

def Calculate(N):
    N = abs(N)
    
    return N  % 10

def main():
    No = int(input("Enter the number : "))

    Ret = Calculate(No)

    print("The last digit of the number is : ",Ret)

if __name__=="__main__":
    main()