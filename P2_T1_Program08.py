# Count the number of vowels in a string.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or
            i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            Count += 1

    print(f"Vowels in the String are : {Count}")

if __name__ == "__main__":
    main()