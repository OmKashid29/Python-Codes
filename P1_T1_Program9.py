# Find the square of a number.

def Square(a):
    return a*a

def main():
    No = int(input("Enter the number : "))
    Ret = Square(No)
    print(f"Square of {No} is {Ret}")

if __name__=="__main__":
    main()