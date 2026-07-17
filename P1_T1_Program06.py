# Input two numbers and print their quotient.

def Quotient(a,b):
    return a // b

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    Ret = Quotient(No1,No2)
    print(f"Quotient of {No1} by {No2} is {Ret}")

if __name__=="__main__":
    main()
