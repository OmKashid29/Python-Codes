# Count lowercase characters.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if ("a" <= i <= "z"):
            Count += 1

    print(f"lowercase in the String are : {Count}")

if __name__ == "__main__":
    main()