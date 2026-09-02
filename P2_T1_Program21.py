# Remove all spaces from a string.

def main():
    String = input("Enter a String : ")

    Result = ""

    for i in String:
        if (i != " "):
            Result += i

    print(f"String after Removing all spaces is : {Result}")

if __name__ == "__main__":
    main()