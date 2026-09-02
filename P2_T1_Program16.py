# Check whether a string is a palindrome.

def main():
    String = input("Enter a String : ")

    Reverse = ""

    for i in String :
        Reverse = i + Reverse

    if (String == Reverse):
        print("String is palindrome")
    else:
        print("String is not palindrome")


if __name__ == "__main__":
    main()