# Calculate Compound Interest.

def Compound_Interset(P,Y,R):
    A = P*((1 + (R/100))**Y)
    return A - P

def main():
    Principal = float(input("Enter the amount : "))
    Years = float(input("Enter the number of year : "))
    Rate = float(input("Enter the rate of interset : "))

    CI = Compound_Interset(Principal,Years,Rate)
    print("Compound insterset is ",CI)

if __name__=="__main__":
    main()