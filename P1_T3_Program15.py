# Electricity bill calculator.

def Calculate(Units):
    Fixed_Rate_Per_Unit = 7.5
    return Units * Fixed_Rate_Per_Unit

def main():
    Units = int(input("Enter the number of units : "))

    Ret = Calculate(Units)

    print(f"The electricity bill is {Ret}")

if __name__=="__main__":
    main()