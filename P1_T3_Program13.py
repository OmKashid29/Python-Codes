# Grade calculator.

def Calculate_Grade(Marks):
    if Marks > 90 :
        return 'A'
    elif Marks > 80 :
        return 'B'
    elif Marks > 70 :
        return 'C'
    elif Marks > 60 :
        return 'D'
    else:
        return 'Fail'

def main():
    Marks = float(input("Enter the marks : "))

    Ret = Calculate_Grade(Marks)

    print(f"Garde is {Ret}")

if __name__=="__main__":
    main()