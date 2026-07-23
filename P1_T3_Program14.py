# Income tax calculator.

def Income_Tax(Income,Income_Tax_Percent):
    return Income_Tax_Percent / 100 * Income

def main():
    Income = int(input("Enter the income : "))
    Income_Tax_Percent = float(input("Enter the % Of tax : "))

    Ret = Income_Tax(Income,Income_Tax_Percent)

    print(f"Income tax is {Ret}")

if __name__=="__main__":
    main()