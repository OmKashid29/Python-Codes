# Print only the vowels from a string.

def main():
    String = input("Enter a String : ")

    Result = ""

    for i in String:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or
            i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            Result += i

    print(f"The vowels from a string are : {Result}")

if __name__ == "__main__":
    main()