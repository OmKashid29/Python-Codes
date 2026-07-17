# Input two numbers and print their difference.

def Difference(a,b):
    return abs(a - b)

def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    Ret = Difference(No1,No2)
    print(f"Difference between {No1} and {No2} is {Ret}")

if __name__ == "__main__":
    main()
