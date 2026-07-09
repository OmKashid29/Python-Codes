# Find the cube of a number.

def Cube(a):
    return a**3

def main():
    No = int(input("Enter the number : "))
    Ret = Cube(No)
    print(f"Cube of {No} is {Ret}")

if __name__=="__main__":
    main()