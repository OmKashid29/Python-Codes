# Print only the digits from a string.

def main():
    String = input("Enter a String : ")

    Result = ""

    for i in String:
        if ("0" <= i <= "9"):
            Result += i

    print(f"The digits from a string. are : {Result}")

if __name__ == "__main__":
    main()