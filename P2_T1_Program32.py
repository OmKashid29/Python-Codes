# Remove duplicate characters from a string.

def main():
    String = input("Enter the string : ")

    Copy = ""

    for i in String:
        if i not in Copy:
            Copy += i

    print(f"After removing duplicates from String : ",Copy)

if __name__=="__main__":
    main()