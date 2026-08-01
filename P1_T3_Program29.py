# BMI calculator.

def BMI(W,H):
    bmi = W / (H**2)
    return bmi

def main():
    Weight = float(input("Enter the weight in kg: "))
    Height = float(input("Enter the height in meter : "))

    Ret = BMI(Weight,Height)

    if Ret >= 30 :
        print(f"BMI is {Ret} which is Obesity")
    elif (25 <= Ret < 30):
        print(f"BMI is {Ret} which is Overweight")
    elif (18.5 <= Ret < 25):
        print(f"BMI is {Ret} which is Healthy weight")
    else:
        print(f"BMI is {Ret} which is Underweight")

if __name__=="__main__":
    main()