# Count how many times a particular character occurs.

def main():
    String = input("Enter a String : ")

    Ch = input("Enter a character ")
    Count = 0 

    for i in String:
        if (Ch == i):
            Count += 1

    print(f"The character {Ch} occured {Count} times in the string")

if __name__ == "__main__":
    main()