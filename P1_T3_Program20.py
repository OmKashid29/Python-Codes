# Check whether a character is a digit.

def Check(N):
    if '0' <= N <= '9':
        return True
    return False

def main():
    No = input("Enter the character : ")

    Ret = Check(No)

    if Ret == True : 
        print(f"{No} is a Digit ")
    else :
        print(f"{No} is not a Digit ")

if __name__=="__main__":
    main()