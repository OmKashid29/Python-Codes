# Check whether three angles form a triangle.

def Check(A1,A2,A3):
    if (A1 + A2 + A3 == 180):
        return True
    return False

def main():
    A1 = float(input("Enter the first angle : "))
    A2 = float(input("Enter the second angle : "))
    A3 = float(input("Enter the third angle : "))

    Ret = Check(A1,A2,A3)

    if Ret == True:
        print("This three angles will form a triangle")
    else :
        print("This three angles will not form a triangle")

if __name__=="__main__":
    main()