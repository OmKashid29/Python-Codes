# Check whether a year is a leap year.

def Leap_Year(Year):
    if Year % 4 == 0 :
        return True
    return False

def main():
    Year = int(input("Enter the year : "))

    Ret = Leap_Year(Year)

    if Ret == True :
        print("Year is a leap year ")
    else:
        print("Year is a not leap year ")

if __name__=="__main__":
    main()