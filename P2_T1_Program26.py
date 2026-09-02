# Print only the alphabets from a string.

def main():
    String = input("Enter a String : ")

    Result = ""

    for i in String:
        if ("A" <= i <= "Z" or "a" <= i <= "z"):
            Result += i

    print(f"the alphabets from a string are : {Result}")

if __name__ == "__main__":
    main()