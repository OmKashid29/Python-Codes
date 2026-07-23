# Check voting eligibility.

def Voting_Eligibility(Age):
    if (Age > 18):
        return True
    return False

def main():
    Age = int(input("Enter the age : "))

    Ret = Voting_Eligibility(Age)

    if Ret == True:
        print("Eligible for voting")
    else:
        print("Not Eligible for voting")

if __name__=="__main__":
    main()