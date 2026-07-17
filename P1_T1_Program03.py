# Input two numbers and print their sum.

def Sum(a,b):
    return a + b

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    Ret = Sum(No1,No2)
    print(f"Sum of {No1} and {No2} is {Ret}")

if __name__=="__main__":
    main()
