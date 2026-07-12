# Convert days into years, months, and days (assume 30-day months, 365-day years).

def Calculate(D):
    Years = D // 365
    D = D % 365
    Months = D // 30
    Days = D % 30
    
    return Years , Months , Days

def main():
    Day = int(input("Enter the Days : "))

    Years , Months , Days = Calculate(Day)

    print(f"{Day} days are {Years} Years {Months} Months and {Days} days")   

if __name__=="__main__":
    main()