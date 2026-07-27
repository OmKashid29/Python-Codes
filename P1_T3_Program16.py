# Calculate bonus based on years of service

def Bonus(Years):
    if Years > 30 :
        return 10000
    elif Years > 25 :
        return 9000
    elif Years > 20 :
        return 8000
    elif Years > 15 :
        return 7000
    elif Years > 10 :
        return 6000
    elif Years > 5 :
        return 5000
    else:
        return 3000

def main():
    Years = int(input("Enter the years of service : "))

    Ret = Bonus(Years)

    print(f"The bonus for {Years} years is {Ret} rupees")

if __name__=="__main__":
    main()