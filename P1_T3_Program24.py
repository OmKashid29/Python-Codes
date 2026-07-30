# Check whether a number is a multiple of 10.

def Multiple(N):
    if (N % 10 == 0):
        return True
    return False

def main():
    No = int(input("Enter the number : "))

    Ret = Multiple(No)

    if Ret == True :
        print(f"{No} is multiple of 10")
    else : 
        print(f"{No} is not multiple of 10")

if __name__=="__main__":
    main()