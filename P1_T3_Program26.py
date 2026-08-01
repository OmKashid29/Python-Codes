# ATM withdrawal simulation.

def Withdrawal_Process(Current_Balance,Withdraw_Amount):
    if (Withdraw_Amount <= 0 ):
        print("Enter the valid amount")

    elif (Withdraw_Amount < 100):
        print("Please enter the minimum withdrawal amount (100)")

    elif (Withdraw_Amount > Current_Balance):
        print("Insuffiecient Balance")

    else:
        Current_Balance = Current_Balance - Withdraw_Amount
        print(f"Amount {Withdraw_Amount} has been withdrawn from the account")
        print(f"The current balance is {Current_Balance}")

def main():
    Current_Balance = 5000
    print(f"The current balance is {Current_Balance}")

    Withdraw_Amount = int(input("Enter the amount to withdraw : "))

    Withdrawal_Process(Current_Balance,Withdraw_Amount)

if __name__=="__main__":
    main()