# Check if two numbers are equal.

def Equal(A,B):
    if A == B :
        return True
    return False

def main():
    No1 = float(input("Enter the first number : "))
    No2 = float(input("Enter the second number : "))

    Ret = Equal(No1,No2)

    if Ret == True :
        print("Numbers are equal")
    else:
        print("Numbers are not equal")

if __name__=="__main__":
    main()
