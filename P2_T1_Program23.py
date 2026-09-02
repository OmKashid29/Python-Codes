# Remove all vowels from a string.

def main():
    String = input("Enter a String : ")

    Result = ""

    for i in String:
        if (i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and
            i != "A" and i != "E" and i != "I" and i != "O" and i != "U"):
            Result += i

    print(f"String after  Remove all vowels is : {Result}")

if __name__ == "__main__":
    main()