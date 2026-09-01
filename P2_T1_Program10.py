# Count the number of spaces in a string.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if (i == " "):
            Count += 1

    print(f"Spaces in the String are : {Count}")

if __name__ == "__main__":
    main()