# Check whether a student passes based on marks in five subjects.

def Result(Sub1,Sub2,Sub3,Sub4,Sub5):
    Average = (Sub1 + Sub2 + Sub3 + Sub4 + Sub5) / 5
    
    if (Average > 40 ):
        return "Pass"
    else :
        return "Fail"

def main():
    Sub1 = int(input("Enter marks in english : "))
    Sub2 = int(input("Enter marks in physics : "))
    Sub3 = int(input("Enter marks in chemistry : "))
    Sub4 = int(input("Enter marks in maths : "))
    Sub5 = int(input("Enter marks in history : "))

    Ret = Result(Sub1,Sub2,Sub3,Sub4,Sub5)

    print(f"Student is {Ret}")

if __name__=="__main__":
    main()