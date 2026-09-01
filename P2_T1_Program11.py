# Count the number of digits in a string.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if ("0" <= i <= "9"):
            Count += 1

    print(f"Digits in the String are : {Count}")

if __name__ == "__main__":
    main()