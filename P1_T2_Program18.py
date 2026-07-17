# Calculate the total salary using basic salary, HRA, and DA.

def Calculate(Basic_Salary,HRA,DA):
    Total_Salary = Basic_Salary + HRA + DA
    return Total_Salary

def main():
    Basic_Salary = float(input("Enter the Basic Salary : "))
    HRA = float(input("Enter the HRA : "))
    DA = float(input("Enter the DA : "))

    Ret = Calculate(Basic_Salary,HRA,DA)

    print(f"The Total Salary is {Ret} ")

if __name__=="__main__":
    main()