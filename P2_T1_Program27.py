# Count the number of words in a sentence.

def main():
    String = input("Enter a String : ")

    Count = 0

    for i in String:
        if ( i == " "):
            Count += 1

    print(f"the number of words in a sentence are : {Count + 1}")

if __name__ == "__main__":
    main()