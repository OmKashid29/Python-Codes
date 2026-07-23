# Find whether a number is divisible by both 5 and 11.

def Check(N):
    if (N % 5 == 0 and N % 11 == 0):
        return True
    return False

def main():
    No = int(input("Enter the number : "))
    Ret = Check(No)

    if Ret == True :
        print(f"{No} is divisible by both 5 and 11")
    else : 
        print(f"{No} is not divisible by both 5 and 11")

if __name__=="__main__":
    main()