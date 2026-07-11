# Find the smallest of two numbers

def Smaller(A,B):
    if A < B:
        return True
    return False

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Ret = Smaller(No1,No2)

    if Ret == True :
        print(f"{No1} is Smaller than {No2}")
    else :
        print(f"{No2} is Smaller than {No1}")
     
if __name__=="__main__":
    main()