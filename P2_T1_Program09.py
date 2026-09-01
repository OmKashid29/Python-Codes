# Count the number of consonants in a string.

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        if (i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and 
           i != "A" and i != "E" and i != "I" and i != "O" and i != "U" and i != " "):
           Count += 1

    print(f"Consonants of the String are : {Count}")

if __name__ == "__main__":
    main()