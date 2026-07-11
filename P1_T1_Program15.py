# Calculate the average of five numbers.

def Average(a,b,c,d,e):
    return (a + b + c + d + e)/5

def main():
    A = float(input("Enter first number : "))
    B = float(input("Enter second number : "))
    C = float(input("Enter third number : "))
    D = float(input("Enter fourth number : "))
    E = float(input("Enter fifth number : "))

    Ret = Average(A,B,C,D,E)

    print(f"Average of numbers {A},{B},{C},{D},{E} is {Ret}")

if __name__=="__main__":
    main()