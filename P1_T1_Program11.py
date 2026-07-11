# Calculate Simple Interest

def Simple_Interset(P,Y,R):
    return  (P*Y*R)/100

def main():
    Principal = float(input("Enter the amount : "))
    Years = float(input("Enter the number of year : "))
    Rate = float(input("Enter the rate of interset : "))

    SI = Simple_Interset(Principal,Years,Rate)

    print("Simple interset is ",SI)

if __name__=="__main__":
    main()