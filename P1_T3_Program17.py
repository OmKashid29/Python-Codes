# Check whether a triangle is valid.

def Triangle(AB,AC,BC):
    if (AB == AC == BC ):
        return 'Equivalient Triangle'
    elif (AB == AC or AB == BC or AC == BC):
        return 'Isolation Triangle'
    else :
        return 'Scaler Triangle'

def main():
    AB = float(input("Enter the first side : "))
    AC = float(input("Enter the second side : "))
    BC = float(input("Enter the third side : "))

    Ret = Triangle(AB,AC,BC)

    print(f"The triangle is {Ret}")

if __name__=="__main__":
    main()