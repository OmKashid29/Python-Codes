# Calculate GST amount and final bill.

def Calculate(Amount,GST_Rate):
    GST_Amount = Amount * GST_Rate / 100
    Final_Bill = GST_Amount + Amount

    return GST_Amount,Final_Bill

def main():
    Amount = float(input("Enter the amount : "))
    GST_Rate = float(input("Enter the GST Rate : "))

    GST_Amount , Final_Bill = Calculate(Amount,GST_Rate)

    print(f"GST Amount is {GST_Amount} \nFinal Bill is {Final_Bill}")

if __name__=="__main__":
    main()