# Print the last character of a string.

def main():
    String = input("Enter the String : ")

    Count = 0

    for i  in String:
        Count += 1

    print(f"The last character of a string is : {String[Count - 1]}")

if __name__ == "__main__":
    main()