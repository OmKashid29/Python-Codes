# Count uppercase characters.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if ("A" <= i <= "Z"):
            Count += 1

    print(f"Uppercase in the String are : {Count}")

if __name__ == "__main__":
    main()