# Find whether a number is divisible by 3 or 7.

def Check(N):
    if (N % 3 == 0 or N % 7 == 0):
        return True
    return False

def main():
    No = int(input("Enter the number : "))
    Ret = Check(No)

    if Ret == True :
        print(f"{No} is divisible by  3 or 7.")
    else : 
        print(f"{No} is not divisible by 3 or 7.")

if __name__=="__main__":
    main()