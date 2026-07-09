# Input two numbers and print their product.

def Product(a,b):
    return a * b

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    Ret = Product(No1,No2)
    print(f"Product of {No1} and {No2} is {Ret}")

if __name__=="__main__":
    main()