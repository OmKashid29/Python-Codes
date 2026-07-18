# Find the smallest of three numbers.

def Smallest(No1,No2,No3):
    if No1 < No2 and No1 < No3 :
        print(f"{No1} is smallest ")
    else :
        if No2 < No3 :
            print(f"{No2} is smallest ")
        else :
            print(f"{No3} is smallest")

def main():
    No1 = float(input("Enter the first number : "))
    No2 = float(input("Enter the second number : "))
    No3 = float(input("Enter the third number : "))

    Smallest(No1,No2,No3)

if __name__=="__main__":
    main()