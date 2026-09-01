# Count the number of characters in a string.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if (i != " "):
            Count += 1

    print(f"Length of the String is : {Count}")

if __name__ == "__main__":
    main()