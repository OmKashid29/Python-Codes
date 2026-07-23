# Check driving eligibility

def Driving_Eligibility(Age):
    if (Age > 18):
        return True
    return False

def main():
    Age = int(input("Enter the age : "))

    Ret = Driving_Eligibility(Age)

    if Ret == True:
        print("Eligible for Driving")
    else:
        print("Not Eligible for Driving")

if __name__=="__main__":
    main()