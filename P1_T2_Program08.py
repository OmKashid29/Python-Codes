# Check whether a number is positive, negative, or zero.

def Check(N):
    if N > 0:
        print("Number is positive")
    elif N == 0 :
        print("Number is zero")
    else:
        print("Number is negative")

def main():
    No = float(input("Enter the number : "))

    Check(No)

if __name__=="__main__":
    main()
