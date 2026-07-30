# Check whether a person gets a discount based on age.

def Discount(N):
    if (N > 60):
        return True
    return False

def main():
    Age = int(input("Enter the Age : "))

    Ret = Discount(Age)

    if Ret == True :
        print(f"{Age} will get discount")
    else : 
        print(f"{Age} will not get discount")

if __name__=="__main__":
    main()